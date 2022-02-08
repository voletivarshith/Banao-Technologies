from .models import User,User_type,City,State
from django.contrib import messages
def signup_validation(request,signup_query_dict,user_type_obj):
    if User.objects.filter(username=signup_query_dict.get("uname")).exists():
            messages.error(request,"Username already exists please try with different username")
            return 0
    if User.objects.filter(email=signup_query_dict.get("useremail")).exists():
        messages.error(request,"Email already exisits")
        return 0
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
    return user_obj