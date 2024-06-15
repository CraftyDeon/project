from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user
def index(request):
    obj=user.objects.all()
    return render(request,"home.html",{'obj':obj})