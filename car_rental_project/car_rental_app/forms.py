# forms.py
from django import forms
from .models import SignupData

class SignupForm(forms.ModelForm):
    class Meta:
        model = SignupData
        fields = ['full_name', 'email', 'phone_number']  # Include specific fields

