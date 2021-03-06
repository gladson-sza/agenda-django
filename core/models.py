from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "event"

    def get_event_date(self):
        return self.event_date.strftime('%d/%m/%Y %H:%M')

    def get_date_input_event(self):
        return self.event_date.strftime('%Y-%m-%dT%H:%M')
