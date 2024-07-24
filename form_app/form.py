from django.forms import fields  
from .models import *  
from django import forms  


class Login_form(forms.ModelForm):

    class Meta:
        model = Login
        fields = '__all__'

