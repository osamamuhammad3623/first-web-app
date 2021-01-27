from django import forms
from django.forms import Form

class customPasswordForm(Form):
    letters = forms.BooleanField(required=False)
    numbers = forms.BooleanField(required=False)
    symbols = forms.BooleanField(required=False)
    passLength = forms.IntegerField(required=True)