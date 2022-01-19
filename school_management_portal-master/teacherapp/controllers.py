from teacherapp import models,serialisers
from rest_framework import serializers, response, parsers, status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from manageapp.models import Teacher

class StudentController:

    def create_student(self,username: str,email: str,password1: str,user: object):
        if(User.objects.filter(email=email).exists()):
            return response.Response({
                "result": False,
                "msg": "email already exsists"
            }, status=status.HTTP_400_BAD_REQUEST)

        stu_obj = User.objects.create(username=username,email=email,is_active=True)
        stu_obj.set_password(password1)
        stu_obj.save()
        token = Token.objects.get_or_create(user=user)[0] 
        tea_obj = Teacher.objects.get(name=user)
        models.Student.objects.create(name=stu_obj,teacher=tea_obj)
        return token, stu_obj

    def take_attendance(self,stu_id: int,present :bool):
        user = User.objects.get(id=stu_id)
        stu_user = models.Student.objects.get(name=user)
        stu_attendence = models.Attendance.objects.create(student=stu_user,presented=present)
        return stu_attendence
    
    def list_student(self,name: str, user: object):
        user_obj = User.objects.get(username=name)
        if(models.Student.objects.filter(name=user_obj).exists()):
            pass
        tea_obj = Teacher.objects.get(name=user)
        stu_data = models.Student.objects.filter(name=user_obj,teacher=tea_obj)
        stu_list =serialisers.StudentSerializer(stu_data,many=True)
        return stu_list
    
    def stu_detail(self,pk: int):
        user_obj = User.objects.get(id=pk)
        stu_obj = models.Student.objects.get(name=user_obj)
        total_absent = models.Attendence.objects.filter(student=stu_obj,present=False).count()
        total_present = models.Attendence.objects.filter(student=stu_obj,present=True).count()
        return user_obj,total_absent,total_present

    def viewhomework(self,user: object):
        stu_obj = models.Student.objects.get(user=user)
        user_obj = User.objects.get(username = stu_obj.teacher.name.username)
        tea_prof = models.TeacherProfile.objects.get(teacher=user_obj) 
        return tea_prof   

class TeachersController:

    def create_homework(self,user: object,homework: str):
        teacher_obj = models.TeacherProfile.objects.get(teacher=user)
        teacher_obj.homework = homework
        teacher_obj.save()
