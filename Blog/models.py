from django.db import models
from users.models import User
from django.utils.text import slugify

class PostCategory(models.Model):
    category = models.CharField(max_length=101)
    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = "Post Categories"

class Post(models.Model):
    title = models.CharField(max_length=101,unique=True)
    image = models.ImageField(upload_to="post_pics",blank=True)
    category = models.ForeignKey(PostCategory,null=True,on_delete=models.SET_NULL)
    post_user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title_slug = models.SlugField(max_length=101)
    content = models.TextField(max_length=5000)
    summary = models.TextField(max_length=501)
    date_time = models.DateTimeField(auto_now_add=True)
    posted = models.BooleanField(default=False)
    def save(self,*args,**kwargs):
        self.title_slug = slugify(self.title,allow_unicode=False)
        super().save(*args,**kwargs)
    def __str__(self):
        return self.title
