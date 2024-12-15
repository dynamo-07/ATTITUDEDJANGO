from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username1')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        name1 = request.POST.get('1name')
        name2 = request.POST.get('2name')
        confirm_password = request.POST.get('confirm-password1')
        if not username or not email or not password:
            messages.error(request, "All fields are required!")
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered!")
                return redirect('signup')
            return redirect('signup')
        
        if password == confirm_password:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name= name1 ,
                last_name= name2,
            )
            user.save()
            return redirect('index')
        else:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')
    return render(request, 'signup.html')

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            mess = "Welcome, " + username
            return render(request, 'index.html', {'message1': mess})  
        return render(request, 'index.html', {'messages': 'Invalid username or password!'})
    return render(request, 'index.html')