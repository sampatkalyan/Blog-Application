from django import forms
from django.forms import fields
from .models import blog
class blogform(forms.ModelForm):
    image = forms.ImageField(required=False, error_messages={
                                       'invalid': ('Image files only')}, widget=forms.FileInput)
    class Meta:
        model = blog
        fields=['title', 'body', 'image', 'category', 'tags']

