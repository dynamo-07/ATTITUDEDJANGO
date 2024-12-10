from django.shortcuts import render
user_data = []
def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        for user in user_data:
            if user['username'] == username and user['password'] == password:
                mess = "welcome "+username
                return render(request, 'index.html', {'message1': mess})
        return render(request, 'index.html', {'message1': 'Invalid username or password!'})
    return render(request, 'index.html')
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username1')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('confirm-password1')
        if password == confirm_password:
            user_data.append({'username': username, 'email': email, 'password': password})
            return render(request, 'index.html', {'message1': 'Registration successful!'})
        else:
            return render(request, 'signup.html', {'message': 'Passwords do not match!'})

    return render(request, 'signup.html')
