from django.db import models
from django.contrib.auth.models import User
from manageapp.models import Teacher
# Create your models here.

class TeacherProfile(models.Model):
    teacher = models.OneToOneField(User,on_delete=models.CASCADE)
    homework = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.teacher.username 

class Student(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name.username

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    datecreated = models.DateField(auto_now_add=True)
    presented = models.BooleanField(default=False)

    def __str__(self):
        return self.student.name.username
                