from django.contrib import admin
from .models import StudentModel,FacultyModel
# Register your models here.
admin.site.register(StudentModel)
admin.site.register(FacultyModel)