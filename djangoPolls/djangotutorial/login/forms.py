from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields=('username', 'email')
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields =('username', 'email', 'first_name', 'last_name', 'is_Active')
        