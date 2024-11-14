from urllib.parse import urlencode
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse

def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        conf_pass = request.POST.get('password2')

        # Check if passwords match
        if password != conf_pass:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')  # Redirect back to the signup page

        # Create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect('signin')

    return render(request, "authentication/signup.html")


def signin(request): 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in first
            # context_data = {'key': user.username}  # You can use first_name or username
            # query_string = urlencode(context_data)
            # return redirect(f"{reverse('home')}?{query_string}")  # Construct the URL correctly
            return redirect('home')  # Construct the URL correctly
        else:
            messages.error(request, "Wrong Credentials")
            return redirect('index')

    return render(request, "authentication/signin.html")

def signout(request):
    pass


def gamerules(request):
    return render(request, "gamerules.html")

def community(request):
    return render(request, "community.html")

def forum(request):
    return render(request, "forum.html")