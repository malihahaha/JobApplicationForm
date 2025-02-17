from django import forms
from .models import JobApplication
import os

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'phone', 'resume', 'cover_letter']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            ext = os.path.splitext(resume.name)[1].lower()
            if ext != '.pdf':
                raise forms.ValidationError("Only PDF files are allowed.")
        return resume
