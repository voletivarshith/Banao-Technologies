from django.contrib import admin
from django.urls import path
from users.views import signup
urlpatterns = [
    path('admin/', admin.site.urls),
    path("sign-up/",signup,name="signup"),
]
