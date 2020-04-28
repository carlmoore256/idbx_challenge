from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import CoordinatorProfile

# add options when registering for first, last name and id
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    institutional_id = forms.IntegerField(label='Institutional ID')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'institutional_id', 'password1', 'password2']
