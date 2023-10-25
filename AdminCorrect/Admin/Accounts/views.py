from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()
def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        role = request.POST["role"]
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exists")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect("register")
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email, password=password1)
                print(role)
                if role == "teacher":
                    user.is_teacher = True
                elif role == "employee":
                    user.is_employee = True
                elif role == "student":
                    user.is_student = True
            user.save()
            password = password1
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("homepage")
        else:
            messages.error(request, "Password do not match")
            return redirect("register")
    return render(request, "register.html")

def homepage(request):
    return render(request, "homepage.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_teacher: #admin
                auth.login(request, user)
                return redirect("admin_homepage")
            else:
                auth.login(request, user)
                return redirect("homepage")
        else:
            messages.info(request, "Invalid username or password")
            return redirect("login")
    return render(request, 'login.html')

def admin_homepage(request):
    return render(request, "admin.html")
        