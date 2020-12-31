from django.views import View
from django.shortcuts import render
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginView()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginView(request.POST)
        return render(request, "users/login.html", {"form": form})
