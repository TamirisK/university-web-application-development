from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView,
    EnrollmentListView, EnrollmentDetailView, EnrollmentCreateView,
    LessonListView, LessonDetailView, LessonCreateView, LessonUpdateView
)

urlpatterns = [
    # Courses
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/create/', CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),

    # Enrollments
    path('enrollments/', EnrollmentListView.as_view(), name='enrollment_list'),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment_detail'),
    path('enrollments/create/', EnrollmentCreateView.as_view(), name='enrollment_create'),

    # Lessons
    path('lessons/', LessonListView.as_view(), name='lesson_list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lessons/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)