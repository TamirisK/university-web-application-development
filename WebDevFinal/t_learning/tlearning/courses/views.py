from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from courses.models import Course, Enrollment, Lesson
from courses.forms import CourseForm, EnrollmentForm, LessonForm


class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'


class CourseCreateView(CreateView):
    model = Course
    fields = ['title', 'description', 'price', 'category', 'instructor']
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')


class CourseUpdateView(UpdateView):
    model = Course
    fields = ['title', 'description', 'price', 'category', 'instructor']
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')


class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'courses/enrollment_list.html'
    context_object_name = 'enrollments'


class EnrollmentDetailView(DetailView):
    model = Enrollment
    template_name = 'courses/enrollment_detail.html'
    context_object_name = 'enrollment'


class EnrollmentCreateView(CreateView):
    model = Enrollment
    fields = ['user', 'course', 'status']
    template_name = 'courses/enrollment_form.html'
    success_url = reverse_lazy('enrollment_list')


class LessonListView(ListView):
    model = Lesson
    template_name = 'courses/lesson_list.html'
    context_object_name = 'lessons'


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'courses/lesson_detail.html'
    context_object_name = 'lesson'


class LessonCreateView(CreateView):
    model = Lesson
    fields = ['course', 'title', 'content', 'video_url']
    template_name = 'courses/lesson_form.html'
    success_url = reverse_lazy('lesson_list')

class LessonUpdateView(UpdateView):
    model = Lesson
    fields = ['title', 'content', 'video_url']
    template_name = 'courses/lesson_form.html'
    success_url = reverse_lazy('lesson_list')
