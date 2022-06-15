from django.contrib import admin
from .models import Path, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Path)