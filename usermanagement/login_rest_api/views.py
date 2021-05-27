from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from guest.guestDAO import GuestDAO
from guest.models import Guest
from django.http import HttpResponse
import requests


def login(request):
    return render(request, 'login.html')
    
    
def get_token(request):
    obj = Guest.objects.get(userid=request.GET['id'])
    user_name = obj.username
    r = requests.post("http://localhost:8000/login/api-jwt-auth/", 
            data={
                "username": user_name,
                "password": request.GET['password']
            })
    return HttpResponse(r)