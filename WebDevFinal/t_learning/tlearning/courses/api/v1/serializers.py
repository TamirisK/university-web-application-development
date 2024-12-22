from rest_framework import serializers
from courses.models import Category, Course, Enrollment, Lesson, Review, Payment, Quiz, QuizQuestion, UserProgress
from users.api.v1.serializers import UserSerializer
from users.models import User




# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


# Course Serializer
class CourseSerializer(serializers.ModelSerializer):
    instructor = UserSerializer()  # Nested UserSerializer
    category = CategorySerializer()  # Nested CategorySerializer

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'category', 'created_at', 'instructor']


# Enrollment Serializer
class EnrollmentSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested UserSerializer
    course = CourseSerializer()  # Nested CourseSerializer

    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'enrollment_date', 'status']


# Lesson Serializer
class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer()  # Nested CourseSerializer

    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'content', 'video_url']


# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested UserSerializer
    course = CourseSerializer()  # Nested CourseSerializer

    class Meta:
        model = Review
        fields = ['id', 'user', 'course', 'rating', 'comment', 'created_at']


# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested UserSerializer

    class Meta:
        model = Payment
        fields = ['id', 'user', 'amount', 'payment_date', 'status']


# Quiz Serializer
class QuizSerializer(serializers.ModelSerializer):
    course = CourseSerializer()  # Nested CourseSerializer

    class Meta:
        model = Quiz
        fields = ['id', 'course', 'title', 'total_marks']


# Quiz Question Serializer
class QuizQuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer()  # Nested QuizSerializer

    class Meta:
        model = QuizQuestion
        fields = ['id', 'quiz', 'question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option']


# User Progress Serializer
class UserProgressSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested UserSerializer
    course = CourseSerializer()  # Nested CourseSerializer

    class Meta:
        model = UserProgress
        fields = ['id', 'user', 'course', 'completed_lessons', 'quiz_scores']
