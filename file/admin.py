from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(FileHandling)
class FileHandlingAdmin(admin.ModelAdmin):
    list_display = ['index','user_id','first_name','last_name','gender','email','phone','d_o_b','job_title']