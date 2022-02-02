from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test,login_required
from users.models import User_type


def doctor_access(user):
    doctor = User_type.objects.get(user_type="Doctor")
    if user.user_type==doctor:
        return True
    else:
        return False

@login_required
def home(request):
    context = {}
    print(Post.objects.all().first().post_user==request.user)
    context['doctor_posts'] = Post.objects.filter(posted=True).exclude(post_user=request.user)
    return render(request,"Blog/home.html",context)

@login_required
@user_passes_test(doctor_access)
def create_post(request):
    form = PostForm()
    context = {'form':form}
    if request.method=="POST":
        form = PostForm(request.POST,request.FILES)
        form.instance.post_user = request.user
        if form.is_valid():
            form.instance.posted = True
            form.save()
            messages.success(request,"Your post is created successfully")
        else:
            context["form"] = form
    return render(request,"Blog/create_post.html",context)