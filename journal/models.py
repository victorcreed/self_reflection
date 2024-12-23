from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #Keep this as not null
    date = models.DateField(auto_now_add=True)
    text = models.TextField() #Keep this as not null
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    intention = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Entry by {self.user} on {self.date}"
