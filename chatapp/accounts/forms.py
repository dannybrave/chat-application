from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist



class SignUpForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control form-control-md',
                'type':'text',
                'id':'username',
                'placeholder':'Enter your username',
            }
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control form-control-md',
                'type':'email',
                'id':'email',
                'placeholder':'Enter your email',
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control form-control-md',
                'type':'password',
                'id':'password',
                'placeholder':'Enter your password',
            }
        )
    )
    
    password2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control form-control-md',
                'type':'password',
                'id':'password',
                'placeholder':'Confirm password',
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control form-control-md',
                'type':'text',
                'id':'username',
                'placeholder':'Enter your username',
            }
        )
    )

    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control form-control-md',
                'type':'password',
                'id':'password',
                'placeholder':'Enter your password',
            }
        )
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            qs = User.objects.filter(username=username)
            user = authenticate(username=username, password=password)
            if not user or not user.is_active:
                raise forms.ValidationError("Invalid login details. Make sure details are correct")
            return self.cleaned_data
        except ObjectDoesNotExist:
            raise forms.ValidationError("Invalid login details. Make sure details are correct ")

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        qs = User.objects.filter(username=username)
        user = authenticate(username=username, password=password)
        return user
