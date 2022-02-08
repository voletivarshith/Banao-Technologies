from .models import User_type
def doctor_access(user):
    doctor_obj = User_type.objects.get(user_type="Doctor")
    if user.user_type==doctor_obj:
        return True
    else:
        return False

def patient_access(user):
    patient_obj = User_type.objects.get(user_type="Patient")
    if user.user_type == patient_obj:
        return True
    else:
        return False