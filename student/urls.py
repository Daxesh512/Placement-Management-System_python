from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'student'

urlpatterns = [
    # home/ or / or student/
    path('student_login/', views.studentlogin, name='student_off'),
    path('auth/', views.auth_view, name='auth'),
    path('edit_details/', views.view_edit, name='edit_page'),
    path('logout/', views.logout, name='logout'),
    
    # Regex patterns for usernames
    re_path(r'users/(?P<username>[A-Za-z_0-9]+)/', views.profile, name='profile'),
    
    # Home and default
    path('home/', views.studentlogin, name='student'),
    path('', views.studentlogin, name='student'),
    
    # Register new student
    path('register/', views.studentregistration, name='student_register'),
    path('listjobs/', views.listjobs, name='list_jobs'),
    path('changed/', views.successfull_change, name='passchgsucc'),
    path('change_password/', views.change_password, name='passchg'),
    path('offer_letter/', views.get_offer, name='offer'),
    path('success/', views.update_details, name="update"),
    path('taken_name/', views.already_taken, name="taken"),
    
    # More regex username patterns
    re_path(r'profile/(?P<username>[A-Za-z_0-9]+)/', views.view_stud_details, name="stud_details"),
    path('download/', views.download, name="download"),
    re_path(r'resume/(?P<username>[A-Za-z_0-9]+)/', views.resumed, name="resumed"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
