from django.db import models

# Create your models here.
class Session_Host(models.Model):
    host_name = models.CharField(max_length=200)
    paid_status = models.IntegerField
    created_date = models.DateTimeField('date created')

class Session_Participant(models.Model):
    participant_name = models.CharField(max_length=200)
    participant_age = models.IntegerField(default=0)
    participant_team = models.CharField(max_length=200)
    participant_location_index = models.IntegerField(default=0)
    created_date = models.DateTimeField('date created')
    session_host = models.ForeignKey(Session_Host, on_delete=models.CASCADE)

