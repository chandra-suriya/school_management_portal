from django.db import models
from django.contrib.auth.models import User

class Standard(models.Model):
    name = models.CharField(max_length=10)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    subject_name = models.OneToOneField(Subject, on_delete=models.CASCADE,
                                        null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name.username
    
