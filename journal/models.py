from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(blank=True) # Allow blank entries
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Entry by {self.user} on {self.date}"
