from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Podaj aktualne hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PasswordForm(forms.Form):
    password = forms.CharField(label='Podaj aktualne hasło', widget=forms.PasswordInput)
    new_password = forms.CharField(label='Podaj nowe hasło', widget=forms.PasswordInput)
    new_password_again = forms.CharField(label='Potwierdź hasło', widget=forms.PasswordInput)