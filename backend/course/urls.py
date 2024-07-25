from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView)
from . import views

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(),name="token-obtain"),
    path('token/refresh/', TokenRefreshView.as_view(), name="refresh-token"),
    path('register/', views.RegisterView.as_view(), name="register-user"),
    path('test/', views.protectedView, name="test"),
    path('courses/', views.CourseView.as_view(), name="course"),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('lessons/', views.LessonView.as_view(), name="lesson"),
    path('quizzes/', views.QuizView.as_view(), name="quiz"),
    path('', views.view_all_routes, name="all-routes")
]
