from django.contrib.auth.forms import UserCreationForm
from apps.users.models import *


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
        	'first_name', 
        	'last_name', 
        	'id_card', 
        	'username', 
        	'role', 
        	'password1', 
        	'password2',
            'birthday', 
            'phone', 
            'email', 
            'address', 
            'is_active',)
        widgets = {
        }