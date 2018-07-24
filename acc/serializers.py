from rest_framework import serializers
from .models import CustomUser
from django.db.models import Q
from rest_framework.serializers import (
    CharField,
    HyperlinkedModelSerializer,
    ModelSerializer,
    ValidationError,
    SerializerMethodField,
)





    


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username')

class UserLoginSerializer(HyperlinkedModelSerializer):
    user_obj = None
    username = CharField(required=True, allow_blank=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        username = data.get('username', None)
        password = data["password"]
        user = CustomUser.objects.filter(
            Q(username=username)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('not valid')

        if user_obj:
            if not user_obj.check_password(password):
               raise ValidationError('wrong pasword')     
        return data


class UserCreateSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'year', 'password')
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user