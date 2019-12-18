from django import forms
from django.contrib.auth.models import User
from .models import Profile

class addProfile(forms.Form):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )
        
class ProfileEditForm(forms.Form):
    class Meta:
        model = Profile
        exclude = ('user', )