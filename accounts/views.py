from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from accounts.forms import SignUpForm
from accounts.token import account_activation_token
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
)
from .forms import UserLoginForm, UserCreationForm, AdminLoginForm

def login_view(request):
    form1 = UserLoginForm(request.POST or None)
    if form1.is_valid():
        username = form1.cleaned_data.get("username")
        password = form1.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not request.user.is_staff:
            login(request, user)
            return redirect("/car/newcar/")
    return render(request, "login.html", {"form": form1, "title": "Đăng Nhập"})

@login_required
def login_admin(request):
    form2 = AdminLoginForm(request.POST or None)
    if form2.is_valid():
        username = form2.cleaned_data.get("username")
        password = form2.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not request.user.is_superuser:
            login(request, user)
            return redirect("/auth")

    return render(request, "login.html", {"form": form2, "title": "Đăng Nhập"})

def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/login/")
    else:
        form = SignUpForm()
    context = {
        "title" : "Đăng Ký",
        "form": form,
    }
    return render(request, "register.html", context)

def logout_view(request):
    logout(request)
    return render(request, "home.html", {})



