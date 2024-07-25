from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    is_student = models.BooleanField(default = True)
    is_teacher = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def profile(self):
        profile = Profile.objects.get(user=self)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000)
    verified = models.BooleanField(default = False)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)


from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    creator = models.ForeignKey(User, default=False, related_name="teacher", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    video_url = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='lessons/files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question = models.CharField(max_length=255, blank=True, null=True)
    answer1 = models.CharField(max_length=255, blank=True, null=True)
    answer2 = models.CharField(max_length=255, blank=True, null=True)
    answer3 = models.CharField(max_length=255, blank=True, null=True)
    answer4 = models.CharField(max_length=255, blank=True, null=True)
    CORRECT_ANSWER_CHOICES = [
        ('answer1', 'Answer 1'),
        ('answer2', 'Answer 2'),
        ('answer3', 'Answer 3'),
        ('answer4', 'Answer 4'),
    ]
    correct_answer = models.CharField(max_length=7, choices=CORRECT_ANSWER_CHOICES, default='answer1')
    def __str__(self):
        return self.question if self.question else 'No Question'
