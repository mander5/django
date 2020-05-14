from django import forms
from django.core import validators
from pro2.models import UserInfo

class NewUserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'
