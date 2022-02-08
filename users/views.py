from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from .models import User,City,State,User_type
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from .validators import signup_validation
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

def home_page(request):
    return render(request,"users/home.html")
@csrf_protect
def signup(request):
    page = request.path.split("/")[-2]
    context = {"page":page}
    if request.method=="POST":
        signup_query_dict = request.POST.copy()
        try:
            user_type_obj = User_type.objects.get(user_type__iexact=page)
        except:
            User_type_obj = None
            return HttpResponse("User type not decleared please contact admin")
        res = signup_validation(request,signup_query_dict,user_type_obj)
        if res==0:
            return redirect("signup-"+page)
        res.save()
        print(res)
        if str(user_type_obj)=="Doctor":
            scopes = ["https://www.googleapis.com/auth/calendar"]
            flow = InstalledAppFlow.from_client_secrets_file("Oauth\\client_secret.json", scopes=scopes)
            creds = flow.run_local_server(server="localhost",port=8004)
            pickle.dump(creds, open(f"Oauth\\{res.id}_token.pkl", "wb"))
        messages.success(request,"Successfully created account now you can login to your account")
        return redirect('login-'+page)
    else:
        return render(request,"users/signup.html",context)

def user_login(request):
    path = request.path.split('/')[2]
    context = {'path':path.title()}
    scopes = ["https://www.googleapis.com/auth/calendar"]
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user_type_obj = User_type.objects.get(user_type__iexact=path)
        except:
            return HttpResponse("User type not decleared please contact admin")
        auth_user = authenticate(request,email=email,password=password,user_type_obj=user_type_obj)
        if auth_user:
            login(request,auth_user)
            return redirect("home")
        else:
            messages.error(request,"Invalid credentials")
            return redirect("login-"+path)
    return render(request,"users/login.html",context)

def dashboard(request):
    return render(request,"users/dashboard.html")