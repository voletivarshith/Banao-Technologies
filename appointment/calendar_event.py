from googleapiclient.discovery import build
import datetime
import pickle
def set_calendar_event(request,date,time,doctor_user):
    start_time = datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]),0)
    end_time = start_time+datetime.timedelta(minutes=45)
    timezone="Asia/Kolkata"
    event = {
        'summary': 'Appointment for you',
        'location': 'Hospital',
        'description': f'An appointment is fixed on {start_time}',
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
            'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 60},
                {'method': 'popup', 'minutes': 10},
            ],
            },
        }
    cred = pickle.load(open(f"Oauth\\{doctor_user.id}_token.pkl",'rb'))
    service = build("calendar","v3",credentials=cred)
    service.events().insert(calendarId="primary",body=event).execute()