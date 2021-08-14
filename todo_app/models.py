from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TODO(models.Model):
    status_choices = [
        ('C', 'Completed'),
        ('NC', 'Not Completed'),
    ]

    priority_choices = [
        ('1', '1️⃣'),
        ('2', '2️⃣'),
        ('3', '3️⃣'),
        ('4', '4️⃣'),
        ('5', '5️⃣'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=3, choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2, choices=priority_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)