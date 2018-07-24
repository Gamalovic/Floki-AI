from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class regform(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'formInput', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'formInput', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'formInput', 'placeholder': 'Last Name'}))
    year = forms.IntegerField(max_value=4, min_value=1, widget=forms.NumberInput(
        attrs={'class': 'formInput', 'placeholder': 'Year'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'formInput', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'formInput', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'year',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(regform, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.year = self.cleaned_data['year']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()

        return user


class logform(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'formInput', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'formInput', 'placeholder': 'Password'}))

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password',
        )


class editform(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control AboutTextarea', 'rows': '15', 'style': 'resize:none;', 'placeholder': 'Write Something About Yourself'}))

    class Meta:
        model = CustomUser
        fields = ('description',)

    def save(self, commit=True):
        user = super(editform, self).save(commit=False)
        user.description = self.cleaned_data['description']

        if commit:
            user.save()

        return user
