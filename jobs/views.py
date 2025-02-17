from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from .models import JobApplication
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def job_application(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your application has been submitted successfully!")
            return redirect('job_application')
        else:
            messages.error(request, "There was an error in your application. Please fix the errors.")
    else:
        form = JobApplicationForm()

    return render(request, 'jobs/application_form.html', {'form': form})
  
