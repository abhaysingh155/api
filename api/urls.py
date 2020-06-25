from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('upcoming_classes/<str:user_name>/', views.upcoming_classes, name="upcoming_classes"),
    path('trial_classes/<str:user_name>/', views.trial_classes, name="trial_classes"),
    path('practice_questions/<str:user_name>/', views.practice_questions, name="practice_questions"),
]
