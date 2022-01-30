from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def signup(request):
    return render(request,"users/signup.html")