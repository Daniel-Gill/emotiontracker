from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    emoji = models.CharField(max_length=2)
    severity = models.IntegerField()
    label = models.CharField(max_length=100)
    
    def __str__(self):
        return self.datetime.strftime("%Y-%m-%d %H:%M:%S") + " " + self.emoji + " " + str(self.severity) + " (" + self.label + ")"