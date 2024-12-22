from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CourseViewSet, EnrollmentViewSet, LessonViewSet, ReviewViewSet, PaymentViewSet, QuizViewSet, QuizQuestionViewSet, UserProgressViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'quiz-questions', QuizQuestionViewSet)
router.register(r'user-progress', UserProgressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
