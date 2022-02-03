from django.shortcuts import render,redirect
from .models import Post,PostCategory
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

@user_passes_test(doctor_access)
def save_post(request):
    context = {}
    context["form"] = PostForm()
    if request.method=="POST":
        title = request.POST.get("title")
        if title:
            try:
                post = Post.objects.get(title__iexact=title)
                messages.error(request,"Post with title already exists")
                return redirect("create-post")
            except:
                pass
            content = request.POST.get("content")
            summary = request.POST.get("summary")
            try:
                post_type = PostCategory.objects.get(category=request.POST.get("category"))
            except:
                post_type=None
            post_obj = Post(title=title,content=content,summary=summary,category=post_type,post_user=request.user)
            if request.FILES.get("image"):
                post_obj.image = request.FILES.get("image")
            post_obj.save()
            messages.success(request,"Post saved successfully you can check this in your Drafts page")
        else:
            messages.error(request,"Title field must be required")
            return redirect("create-post")
    return redirect('create-post')

@login_required
@user_passes_test(doctor_access)
def your_posts(request):
    context = {"posts":Post.objects.filter(post_user=request.user)}
    return render(request,"Blog/your_posts.html",context)

@login_required
@user_passes_test(doctor_access)
def drafts(request):
    context = {"posts":Post.objects.filter(posted=False)}
    return render(request,"Blog/drafts.html",context)