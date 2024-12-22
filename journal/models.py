from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    mushaiba_reflection = models.TextField(blank=True)
    tazkiya_reflection = models.TextField(blank=True)

    def __str__(self):
        return f"Entry by {self.user} on {self.date}"
