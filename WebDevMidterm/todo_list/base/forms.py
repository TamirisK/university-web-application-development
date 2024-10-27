from django import forms
from .models import Task

class PositionForm(forms.Form):
  position = forms.CharField()

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['title', 'description', 'complete', 'category', 'deadline']
    widgets = {
      'deadline': forms.DateInput(attrs={'type': 'date'}),
    }
