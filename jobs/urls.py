from django.urls import path
from .views import home, job_application

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('apply/', job_application, name='job_application'),  # Job application form
]

