from django.db import models
from users.models import User
import datetime
class Speciality(models.Model):
    speciality = models.CharField(max_length=101)
    def __str__(self):
        return self.speciality
    def save(self,*args,**kwargs):
        self.speciality = self.speciality.title()
        super().save(*args,**kwargs)


class Appointments(models.Model):
    speciality = models.ForeignKey(Speciality,on_delete=models.PROTECT)
    appointment_date = models.DateField()
    appointment_start_time = models.TimeField()
    appointment_end_time = models.TimeField()
    patient = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    doctor = models.ForeignKey(User,on_delete=models.CASCADE,related_name="doctor")
    def __str__(self):
        return f"{self.patient}+' '+{self.doctor}"

    def save(self,*args,**kwargs):
        start_time = self.appointment_start_time
        delta = datetime.timedelta(minutes=45)
        print(start_time,delta)
        end_time = (datetime.datetime.combine(datetime.date(1,1,1),start_time)+delta).time()
        self.appointment_end_time = end_time
        super().save(*args,**kwargs)