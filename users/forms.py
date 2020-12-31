from django import forms


class LoginView(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
