from django import forms
from .models import Guest, Book

class RestrictForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'restricted_status', 'restricted_period']