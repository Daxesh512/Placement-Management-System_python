from django.urls import path
from student import views

app_name = 'home'

urlpatterns = [
    # home/ or /
    path('', views.studentlogin, name='home'),
    path('home/', views.studentlogin, name='home'),
]
