from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms.models import ModelForm
from .models import CustomUser

class Registrationform(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':" Enter The Password"}))
    confirm_password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = CustomUser
        fields= ['email', 'username', 'password']

    def confirm_password1(self):
        cleaned_data=super(Registrationform, self).clean()
        password= cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("password does not match")
        