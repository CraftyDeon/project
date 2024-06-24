from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
def index(request):

    return render(request,"home.html",{"logout":logout})
def form(request):
    if request.method == "POST":
        x = request.POST['firstname']
        y = request.POST['lastname']
        z = request.POST['username']
        w = request.POST['email']
        a = request.POST['password1']

        # Check if the username or email already exists
        if User.objects.filter(username=z).exists():
            print("User not created: Username already exists")
            return HttpResponse("Username already exists.")
        elif User.objects.filter(email=w).exists():
            print("User not created: Email already exists")
            return HttpResponse("Email already exists.")
        else:
            # Create and save the user if the conditions are met
            user = User.objects.create_user(username=z, password=a, email=w, first_name=x, last_name=y)
            user.save()
            print("User created")
            return redirect('/')

    return render(request, 'form.html')
def login(request):
    if request.method=="POST":
        p=request.POST["username"]
        q=request.POST["password"]
        user=auth.authenticate(username=p,password=q)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"user not found")
            return redirect("login")
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')