from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Medicine(models.Model):
    name=models.CharField(max_length=200)
    dosage=models.CharField(max_length=200)
    frequency=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=('-date_created',)
    def __str__(self):
        return self.name
    
