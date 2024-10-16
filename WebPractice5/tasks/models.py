from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(_("email address"), unique=True)

    def __str__(self):
        return self.email
    
class Tasks(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, max_length=150)
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='taks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Categories(models.Model):
    title = models.CharField(max_length=20)