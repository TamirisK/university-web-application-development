from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
  CATEGORY_CHOICES = [
    ('Work', 'Work'),
    ('Personal', 'Personal'),
    ('Other', 'Other')
  ]

  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  title = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  complete = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)
  category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
  deadline = models.DateTimeField(null=True, blank=True)

  def __str__(self):
    return self.title

  class Meta:
    order_with_respect_to = 'user'