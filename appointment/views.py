from django.shortcuts import render,redirect
from appointment.models import Speciality,Appointments
from users.decorators import patient_access
from users.models import User,User_type
from django.contrib.auth.decorators import user_passes_test,login_required
from django.views.decorators.csrf import csrf_exempt
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from django.contrib import messages
from .calendar_event import set_calendar_event
import datetime
import pickle

@user_passes_test(patient_access)
def doctors(request):
    context = {}
    doctor_obj = User_type.objects.get(user_type="Doctor")
    doctors = User.objects.filter(user_type=doctor_obj)
    context = {"doctors":doctors}
    return render(request,"appointment/doctors.html",context)


@login_required()
@user_passes_test(patient_access)
@csrf_exempt
def book_appointment(request,doctor):
    context = {}
    try:
        doctor_user = User.objects.get(username=doctor)
        doctor_obj = User_type.objects.get(user_type="Doctor")
        if doctor_user.user_type!=doctor_obj:
            messages.error(request,"Invalid")
            return redirect("doctors")
    except:
        messages.error(request,"Doctor details not found")
        return redirect("doctors")
    if request.method=="POST":
        speciality = request.POST.get("speciality")
        date = request.POST.get("app_date").split("-")
        time = request.POST.get("app_time").split(":")
        date_obj = datetime.datetime(int(date[0]), int(date[1]),int(date[2]))
        time_obj = datetime.time(int(time[0]),int(time[1]))
        print(date_obj,time_obj)
        try:
            speciality_obj = Speciality.objects.get(speciality=speciality)    
        except:
            messages.error(request,"Speciality not available")
            return redirect("doctors")
        appointment_obj = Appointments(speciality=speciality_obj,appointment_date=date_obj,appointment_start_time=time_obj)
        appointment_obj.patient = request.user
        appointment_obj.doctor = doctor_user
        appointment_obj.save()
        #have to add google calander event function
        set_calendar_event(request,date,time,doctor_user,)
        messages.success(request,"Your appointment has booked successfully")
        print(str(appointment_obj.appointment_start_time))
        context = {"appointment_obj":appointment_obj}
        return render(request,"appointment/confirmation.html",context)
    today = datetime.date.today()+datetime.timedelta(days=1)
    context["min_date"] = f"{today.year}-{str(today.month).zfill(2)}-{str(today.day).zfill(2)}"
    today = today + datetime.timedelta(days=30)
    context["max_date"] = f"{today.year}-{str(today.month).zfill(2)}-{str(today.day).zfill(2)}"
    context["speciality"] = Speciality.objects.all()
    context["doctor_user"] = doctor_user
    return render(request,"appointment/book_appointment.html",context)


def testing(request):
  scopes = ['https://www.googleapis.com/auth/calendar']
  flow = InstalledAppFlow.from_client_secrets_file("Oauth\\client_secret.json", scopes=scopes)
  creds = flow.run_local_server(server="localhost",port=8004)
  pickle.dump(creds, open("token.pkl", "wb"))
  credentials = pickle.load(open("token.pkl", "rb"))
  service = build("calendar", "v3", credentials=credentials)
  result = service.calendarList().list().execute()
  start_time = datetime.datetime(2019, 5, 12, 19, 30, 0)
  end_time = start_time + datetime.timedelta(hours=4)
  timezone="Asia/Kolkata"
  
  calendar_id = service.calendarList().list().execute()["items"]
  print(calendar_id)
  # print(service.calendarList().get(calendarId="calendar_id").execute())
  service.events().insert(calendarId="varshithvoleti@gmail.com", body=event).execute()

  return redirect("home")
