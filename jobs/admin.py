from django.contrib import admin
from .models import JobApplication

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'status', 'applied_at')
    list_filter = ('status', 'applied_at')
    search_fields = ('name', 'email', 'phone')

admin.site.register(JobApplication, JobApplicationAdmin)

