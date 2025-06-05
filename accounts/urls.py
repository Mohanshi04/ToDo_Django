from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_home, name='todo_home'),
    path('emailsignin/', views.SendSignInEmail.as_view(), name='email_signin'),
    path('verify-email/<uidb64>/<token>/', views.verify_email, name='verify_email'),
]