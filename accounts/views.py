from time import sleep

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        repassword = request.POST['re_pass']

        if password == repassword:
            if not User.objects.filter(username=name).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=name,
                                                    password=password,
                                                    email=email,
                                                    )
                    user.save()
                    print("User created!")
                    messages.info(request, "Registration successful")
                    sleep(2)
                    return redirect("login")
                else:
                    messages.error(request, "Email already registered.")
                    print("Email already registered")
            else:
                messages.error(request, "Username already taken.")
                print("Username already taken.")
        else:
            messages.error(request, "Passwords do not match")
            print("Passwords do not match")
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        name = request.POST['your_name']
        password = request.POST['your_pass']

        user = auth.authenticate(username=name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials!")
            print("Invalid Credentials")
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")
