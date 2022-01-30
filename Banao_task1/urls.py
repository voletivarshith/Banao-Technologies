from django.contrib import admin
from django.urls import path
from users.views import home,signup,user_login,dashboard
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/',admin.site.urls),
    path('',home,name="home"),
    path("signup/patient/",signup,name="signup-patient"),
    path("signup/doctor/",signup,name="signup-doctor"),
    path("login/patient/",user_login,name="login-patient"),
    path("login/doctor/",user_login,name="login-doctor"),
    path("dashboard/",dashboard,name="dashboard")
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)