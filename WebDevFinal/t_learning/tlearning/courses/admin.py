from django.contrib import admin
from .models import Course, Category, Enrollment, Lesson, Review, Payment, Quiz, QuizQuestion, UserProgress

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'instructor', 'price', 'created_at')
    search_fields = ('title', 'description', 'instructor__username')

admin.site.register(Course, CourseAdmin)
admin.site.register(Category)
admin.site.register(Enrollment)
admin.site.register(Lesson)
admin.site.register(Review)
admin.site.register(Payment)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(UserProgress)
