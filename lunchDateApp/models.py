from django.db import models

# Create your models here.
class Session_Host(models.Model):
    host_name = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')

class Session_Participant(models.Model):
    participant_name = models.CharField(max_length=200)
    participant_age = models.IntegerField
    session_host = models.ForeignKey(Session_Host, on_delete=models.CASCADE)
