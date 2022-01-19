from django.shortcuts import render
import manageapp.models as managemodels
from rest_framework import views, permissions
from django.contrib.auth.models import User
from django.db.models import Q
from teacherapp import controllers
from rest_framework import serializers, response, parsers, status
from django.core import validators
from rest_framework.authtoken.models import Token

# Create your views here.
class TeacherSignin(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        data = request.data
        email_id = data.get("email")
        password = data.get("password")
        if not email_id or not password:
            return response.Response({
                "result": False,
                "msg": "Email or password is missing"
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email_id, is_active=True)
        except exceptions.ObjectDoesNotExist:
            return response.Response(
                {
                    "result": False,
                    "msg": "User Does not exist"
                },
                status=status.HTTP_400_BAD_REQUEST,
                )
        if not user.is_staff:
            return response.Response(
                {
                    "result": False,
                    "msg": "Permission denied"
                },
                status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            is_valid = user.check_password(password)
            if not is_valid:
                return response.Response(
                    {
                        "result": False,
                        "msg": "Enter valid email and password"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                token = Token.objects.get_or_create(user=user)[0]
                return response.Response({
                    "result": True,
                    "msg": "success",
                    "data": {
                        "userid": user.pk,
                        "token": token.key,
                        "username": user.username,
                        "email": user.email,
                    }}, status=status.HTTP_200_OK,
                )

class CreateStudent(views.APIView):

    def post(self, request):
        user = request.user
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')

        if not(user.is_staff):
            return response.Response(
                {
                    "result": False,
                    "msg": "Permission denied"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        if(not username or not email or
           not password1 or not password2):
            return response.Response({
                "result": False,
                "msg": "username or password is missing"
            }, status=status.HTTP_400_BAD_REQUEST)

        if(password1 != password2):
            return response.Response({
                "result": False,
                "msg": "password is not equal "
            }, status=status.HTTP_400_BAD_REQUEST)
        student =  controllers.StudentController()
        token_val,stu_val = student.create_student(username, email, password1,user)
        return response.Response(
                {
                    "result": True,
                    "msg": "Student created",
                },
                status=status.HTTP_200_OK,
            )

class StudentAttendees(views.APIView):

    def post(self, request):
        user = request.user
        data = request.data
        student_id = data.get('student id')
        present = data.get('present')
        if not(user.is_staff):
            return response.Response(
                {
                    "result": False,
                    "msg": "Permission denied"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        student =  controllers.StudentController()
        stu_values = student.take_attendance(student_id, present)
        return response.Response(
                {
                    "result": True,
                    "msg": "Attendence added",
                    "present":stu_values.presented,
                    "attendence id":stu_values.id
                },
                status=status.HTTP_200_OK,
            )
           
class StudentList(views.APIView):

    def post(self,request):
        user = request.user
        data = request.data
        name = data.get('name')
        if not(user.is_staff):
            return response.Response(
                {
                    "result": False,
                    "msg": "Permission denied"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        student =  controllers.StudentController()
        stu_values1 = student.list_student(name,user)
        return response.Response(
                {
                    "result": True,
                    "data":stu_values1.data
                },
                status=status.HTTP_200_OK,
            ) 
      
        
class StudentProfile(views.APIView):

    def get(self,request,pk):
        user = request.user
        if not(user.is_staff):
            return response.Response(
                {
                    "result": False,
                    "msg": "Permission denied"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        student =  controllers.StudentController()
        user_obj, total_absent, total_present = student.stu_detail(pk)  
        return response.Response(
            {
                "result": True,
                "name": user_obj.username,
                "email": user_obj.email,
                "no of days leave":total_absent,
                "no of days present":total_present
            },
            status=status.HTTP_200_OK,
        )
        
class AddHomework(views.APIView):
    
    def post(self, request):
        user = request.user
        data = request.data
        homework = data.get('homework')
        if not(user.is_staff):
            return response.Response(
                {
                    "result": False,
                    "msg": "Permission denied"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        teacher =  controllers.TeachersController()
        teacher.add_homework(homework)
        return response.Response(
            {
                "result": True,
                "msg":"Home work has been created "
            },
            status=status.HTTP_200_OK,
        )

class ViewHomework(views.APIView):

    def get(self, request):
        user = request.user
        if (user.is_staff and user.is_superuser):
            return response.Response(
                {
                    "result": False,
                    "msg": "Permission denied"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        student = controllers.StudentController()
        stu_homework = student.viewhomework(user)    
        return response.Response(
                {
                    "result": True,
                    "msg": stu_homework.homework
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
