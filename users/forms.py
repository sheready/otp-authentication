from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from users.models import User

class UserCreationForm(BaseUserCreationForm):
    phone = forms.CharField(max_length=20, required=True, help_text='Phone number')

    class Meta:
        model = User
        fields = ('username','phone','password1','password2')


class VerifyForm(forms.Form):
    code = forms.CharField(max_length=8, required=True, help_text='Enter OTP Code')

class ResendCodeForm(forms.Form):
    phone = forms.CharField(max_length=20, required=True, help_text='Insert same Phone number used to register account')