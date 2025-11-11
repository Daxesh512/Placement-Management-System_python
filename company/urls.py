from django.urls import path, re_path
from . import views

app_name = 'company'

urlpatterns = [
    path('signup', views.post_list, name='signup_page'),
    path('login', views.view_home, name='login_page'),
    path('edit', views.view_edit, name='home_page'),
    path('verify', views.verify, name='verify_page'),
    re_path(r'^userc/(?P<username>[A-Za-z_0-9]+)/$', views.profile, name='profile'),
    path('jobreqs', views.Jobreqs, name='job_requirements'),
    path('change_password', views.change_password, name='passchg'),
    path('changed', views.successfull_change, name='passchgsucc'),
    path('listjobs', views.listjobs, name='listjobs'),
    re_path(r'^jobs/(?P<jobid>[0-9]+)/$', views.jobdesc, name='jobdesc'),
    path('applied_msg/', views.jobapplied, name='jobapplied'),
    re_path(r'^student_list/(?P<jobid>[0-9]+)/$', views.view_student_list, name='studlist'),
    path('taken_name/', views.already_taken, name="takenc"),
    re_path(r'^offered/(?P<userid>[A-Za-z_0-9]+)/$', views.offered, name="takenc"),
]
