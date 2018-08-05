from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import login
from acc.forms import regform,editform
from rest_framework import generics
from rest_framework.permissions import AllowAny
from acc.serializers import UserCreateSerializer

from django.contrib.auth import get_user_model
#from acc.FinalFinalTest import AIML

#from acc.pyaiml3 import test

#from acc.chatbotTensorFlow.chatbot import dialog
from acc.AIML.Floki import dialogAiml
from acc.AIML.NLP import Filtering
from events.models import Event


from django.core.serializers import serialize
from schedule.models import schedule

import json

from .models import CustomUser

from django.http.response import HttpResponseNotAllowed
from django.urls import reverse_lazy

from rest_framework.views import APIView
from rest_framework import status


from rest_framework.response import Response
from acc.serializers import UserSerializer
from acc.serializers import UserLoginSerializer



from django.contrib.auth.models import User
from rest_framework import viewsets
from django.views import generic
from django.http.response import HttpResponse
#################################################################################
############## Annoying imports #################################################
#################################################################################



class FlokiBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'floki':
            print("success !")
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')



class Msg(APIView):
    #serializer_class = MsgSerializer
   
    ## TensorFlow 
    ##def post(self, request):
    ##    message  = request.data['name']
        # serializer = UserLoginSerializer(data=data)
        # if serializer.is_valid(raise_exception=True):
        #     new_data = serializer.data
        #     print(new_data)

    ##    if request.method=='POST':
            #message_respond = dialog('hello')
    ##        res=dialog(message)
    ##        print(res)
    ##        return Response(res)
        #return Response(serializer.errors)



    ## AIML

    def post(self, request):
        message  = request.data['name']

        filtered_Message=Filtering(message)
        if(filtered_Message =="schedule"):
            queryset = schedule.objects.all()
            r=serialize('json', queryset)
            jsonData=json.loads(r)
            response={"data":jsonData,"source":"db"}
            return Response(json.dumps(response))
            
        
        elif(filtered_Message=="event"):
            queryset = Event.objects.all()
            r = serialize('json', queryset)
            jsonData = json.loads(r)
            response={"data":jsonData,"source":"event"}
            return Response(json.dumps(response))
            

        else:
            if request.method=='POST':
            
                res=dialogAiml(message)
                response={"data":res,"source":"AI"}
                return Response(json.dumps(response))
        
################################### sign up API #######################################

class userCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = CustomUser.objects.all()
    
    
    

################################### login API  ########################################


class userLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        if request.method=='POST':
            data = request.data
            serializer = UserLoginSerializer(data=data)
            queryset = Event.objects.all()
            r = serialize('json', queryset)
            username=request.data['username']
            unRef=CustomUser.objects.all().filter(username=username)
            unData=serialize('json', unRef)

            jsonEventData = json.loads(r)
            jsonUserData = json.loads(unData)
            response={"event":jsonEventData,"userData":jsonUserData}
            if serializer.is_valid(raise_exception=True):
                new_data = serializer.data
                print(new_data)            
            return Response(json.dumps(response))


class userView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


