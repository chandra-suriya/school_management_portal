from django.contrib import admin
from teacherapp import models
# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Attendance)