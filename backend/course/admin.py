
from django.contrib import admin
from .models import Profile, User , Course, Lesson , Quiz
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email']

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['full_name', 'user', 'verified']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','created_at']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'creator']

class QuizAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'question','answer1','answer2','answer3','answer4','correct_answer']

admin.site.register(User,UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Quiz,QuizAdmin)

