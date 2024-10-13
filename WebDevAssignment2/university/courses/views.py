from django.shortcuts import render
from .models import Student, Course

def student_list(request):
    students = Student.objects.all()
    return render(request, 'courses/student_list.html', {'students': students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})