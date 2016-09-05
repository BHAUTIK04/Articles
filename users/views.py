from django.shortcuts import render, redirect
import json
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import (authenticate, get_user_model, login, logout,)
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegisterForm

@csrf_exempt
def register_view(request):
    try:
        print(request.user.is_authenticated())
        next = request.GET.get('next')
        title = "Register"
        if request.method=="POST":
            print "i am here"
	    data = json.loads(request.body)
            avail = User.objects.filter(username=data["email"]).count()
            print avail
	    if avail>0:
                return HttpResponse(json.dumps({"flag":"Error","msg":"Email already Exists"}))
            else:
                print "Here"
                #user = User()
                user=User.objects.create_user(username=data["email"], password=data["password1"], email=data["email"])
                user.first_name=data["firstname"]
                user.last_name=data["lastname"]
                user.save()
                user_auth = authenticate(username=data["email"], password=data["password1"])
                login(request, user_auth)
                return HttpResponse(json.dumps({"flag":"Success","msg":"Register Successfully"}))
        else:
            return render(request, "register.html")
    except Exception as e:
	print str(e)
        return HttpResponse(json.dumps({"flag":"Error","msg":"Something went wrong. Please try again"}))
    
@csrf_exempt
def login_view(request):
    try:
        if request.method=="POST":
            if request.user.is_authenticated():
                print "already loggedin"
                return HttpResponse(json.dumps({"flag":"Warning","msg":"Already loggedin"}))
            else:
                print "i am here"
                data = json.loads(request.body)
                username = data["email"]
                password = data["password"]
                user = authenticate(username=username, password=password)
                login(request, user)
                
                return HttpResponse(json.dumps({"flag":"Success","msg":"SuccessFully Loggedin"}))
        else:
            return render(request, "login.html")
    except Exception as e:
        return HttpResponse(json.dumps({"flag":"Error","msg":"Something went wrong. Please try again"}))
    
def logout_view(request):
    logout(request)
    return redirect('/login/')
