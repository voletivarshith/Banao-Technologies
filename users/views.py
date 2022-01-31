from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from .models import User,City,State,User_type
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
def home(request):
    return render(request,"users/home.html")
def signup_validation(request,signup_query_dict,user_type_obj):
    if User.objects.filter(username=signup_query_dict.get("uname")).exists():
            messages.error(request,"Username already exists please try with different username")
            return 1
    if User.objects.filter(email=signup_query_dict.get("useremail")).exists():
        messages.error(request,"Email already exisits")
        return 1
    city_obj,created = City.objects.get_or_create(city=signup_query_dict.get("city").title())
    state_obj,created = State.objects.get_or_create(state=signup_query_dict.get("state").title())
    user_obj = User(
        first_name = signup_query_dict.get("fname",default=''),
        last_name = signup_query_dict.get("lname",default = ''),
        username = signup_query_dict.get("uname"),
        email = signup_query_dict.get("useremail"),
        line1 = signup_query_dict.get("add_line"),
        city = city_obj,
        state = state_obj,
        pincode = signup_query_dict.get("pincode"),
    )
    if request.FILES.get("profile_pic"):
        user_obj.profile_pic = request.FILES.get("profile_pic")
    user_obj.set_password(signup_query_dict.get("password1"))
    user_obj.user_type = user_type_obj
    user_obj.save()
    return 0
@csrf_protect
def signup(request):
    page = request.path.split("/")[-2]
    context = {"page":page}
    if request.method=="POST":
        signup_query_dict = request.POST.copy()
        try:
            user_type_obj = User_type.objects.get(user_type__iexact=page)
        except:
            return HttpResponse("User type not decleared please contact admin")
        res = signup_validation(request,signup_query_dict,user_type_obj)
        if res:
            return redirect("signup-"+page)
        messages.success(request,"Successfully created account now you can login to your account")
        return redirect('login-'+page)
    else:
        return render(request,"users/signup.html",context)

def user_login(request):
    path = request.path.split('/')[2]
    context = {'path':path}
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user_type_obj = User_type.objects.get(user_type__iexact=path)
        except:
            return HttpResponse("User type not decleared please contact admin")
        auth_user = authenticate(request,username=email,email=email,password=password,user_type_obj=user_type_obj)
        if auth_user:
            login(request,auth_user)
            return redirect("dashboard")
        else:
            messages.error(request,"Invalid credentials")
            return redirect("login-"+path)
    return render(request,"users/login.html",context)

def dashboard(request):
    return render(request,"users/dashboard.html")