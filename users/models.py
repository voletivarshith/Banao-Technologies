from django.db import models
from django.contrib.auth.models import AbstractUser

class City(models.Model):
    city = models.CharField(max_length=101)
    def __str__(self):
        return self.city
    def save(self,*args,**kwargs):
        self.city = self.city.title()
        super().save(*args,**kwargs)
    class Meta:
        verbose_name_plural = "Cities"

class State(models.Model):
    state = models.CharField(max_length = 101)
    def __str__(self):
        return self.state
    def save(self,*args,**kwargs):
        self.state = self.state.title()
        super().save(*args,**kwargs)

class User_type(models.Model):
    user_type = models.CharField(max_length=101)
    def __str__(self):
        return self.user_type

class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to="profile_pics",default="default_img.png")
    # Address fields
    line1 = models.CharField(max_length=1001,blank=True)
    city = models.ForeignKey(City,on_delete=models.PROTECT,null=True,blank=True)
    state = models.ForeignKey(State,on_delete=models.PROTECT,null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    # Doctor or patient
    user_type = models.ForeignKey(User_type,on_delete=models.PROTECT)
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
