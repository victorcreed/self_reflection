from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(blank=True) # Allow blank entries
    intention = models.TextField(blank=True)
    gratitude = models.TextField(blank=True)
    patience = models.TextField(blank=True)
    humility = models.TextField(blank=True)
    awareness = models.TextField(blank=True)
    spiritual_practice = models.TextField(blank=True)
    interactions = models.TextField(blank=True)
    personal_improvement = models.TextField(blank=True)
    gratitude_blessings = models.TextField(blank=True)
    accountability = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Entry by {self.user} on {self.date}"
