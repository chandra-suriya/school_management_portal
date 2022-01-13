from django.shortcuts import render
from manageapp import models, controllers, serialisers
from rest_framework import views, permissions
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import serializers, response, parsers, status
from django.core import validators
from rest_framework.authtoken.models import Token
# Create your views here.

class StandardView(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self,request):
        user = request.user
        data = request.data
        standard = data.get('standard')
        if not (user.is_superuser):
            return response.Response({
                "msg":"user permission is not allowed",
                "result":"false"
            }, status=status.HTTP_400_BAD_REQUEST)
        standard_query = controllers.StandardController()
        std_id = standard_query.create_standard(standard=standard)
        return response.Response({
                "id": std_id,
                "msg": "created standard",
                "result": True,
               }
            )
    def get(self,request):
        user = request.user
        if not (user.is_superuser):
            return response.Response({
                "msg":"user permission is not allowed",
                "result":"false"
            }, status=status.HTTP_400_BAD_REQUEST)
        standard_query = controllers.StandardController()
        std_values = standard_query.get_standard()
        std_list = serialisers.StandardSerializer(std_values, many=True)
        return response.Response({
                "data": std_list.data,
                "result": True,
               }
            )    
    def put(self,request,pk):
        user = request.user
        data = request.data
        standard = data.get('standard')
        if not (user.is_superuser):
            return response.Response({
                "msg":"user permission is not allowed",
                "result":"false"
            }, status=status.HTTP_400_BAD_REQUEST)
        standard_query = controllers.StandardController()  
        std_update = standard_query.update_standard(pk,standard)
        return response.Response({
                "data": std_update,
                "result": True,
               }
            )    
    def delete(self,request,pk):
        user = request.user
        data = request.data
        standard = data.get('standard')
        if not (user.is_superuser):
            return response.Response({
                "msg":"user permission is not allowed",
                "result":"false"
            }, status=status.HTTP_400_BAD_REQUEST)
        standard_query = controllers.StandardController()  
        std_update = standard_query.delete_standard(pk,standard)
        return response.Response({
              "msg":"standard deleted",
                "result": True,
               }
            )

class SubjectView(views.APIView):

    permission_classes = [permissions.IsAdminUser]

    def post(self,request):
        user = request.user
        data = request.data
        subject = data.get('subject')
        if not (user.is_superuser):
            return response.Response({
                "msg":"user permission is not allowed",
                "result":"false"
            }, status=status.HTTP_400_BAD_REQUEST)
        standard_query = controllers.SubjectController()
        std_id = standard_query.create_subject(subject=subject)
        return response.Response({
                "id": std_id,
                "msg": "created subject",
                "result": True,
               }
            )
    def get(self,request):
        user = request.user
        if not (user.is_superuser):
            return response.Response({
                "msg":"user permission is not allowed",
                "result":"false"
            }, status=status.HTTP_400_BAD_REQUEST)
        standard_query = controllers.SubjectController()
        std_values = standard_query.get_subject()
        std_list = serialisers.SubjectSerializer(std_values, many=True)
        return response.Response({
                "data": std_list.data,
                "result": True,
               }
            )    
    def put(self,request,pk):
        user = request.user
        data = request.data
        subject = data.get('subject')
        if not (user.is_superuser):
            return response.Response({
                "msg":"user permission is not allowed",
                "result":"false"
            }, status=status.HTTP_400_BAD_REQUEST)
        standard_query = controllers.SubjectController()  
        std_update = standard_query.update_subject(pk,subject)
        return response.Response({
                "data": std_update,
                "result": True,
               }
            )    
    def delete(self,request,pk):
        user = request.user
        data = request.data
        subject = data.get('subject')
        if not (user.is_superuser):
            return response.Response({
                "msg":"user permission is not allowed",
                "result":"false"
            }, status=status.HTTP_400_BAD_REQUEST)
        standard_query = controllers.SubjectController()  
        std_update = standard_query.delete_subject(pk,subject)
        return response.Response({
              "msg":"subject deleted",
                "result": True,
               }
            )

class TeacherView(views.APIView):
    #permission_classes = [permissions.IsAdminUser]

    def post(self,request):
        user = request.user
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')
        if not (user.is_superuser):
            return response.Response({
                "msg":"user permission is not allowed",
                "result":"false"
            }, status=status.HTTP_400_BAD_REQUEST)
        if(not username or not email or
           not password1 or not password2):
            return response.Response({
                "result": False,
                "msg": "username or password is missing"
            }, status=status.HTTP_400_BAD_REQUEST)
        if (validators.validate_email(email)):
            return response.Response({
                "result": False,
                "msg": "No email id is there"
            }, status=status.HTTP_400_BAD_REQUEST)
        if(User.objects.filter(Q(username=username) | Q(email=email))
           .exists()):
            return response.Response({
                "result": False,
                "msg": "user name or email already exsists"
            }, status=status.HTTP_400_BAD_REQUEST)
        if(password1 != password2):
            return response.Response({
                "result": False,
                "msg": "password is not equal "
            }, status=status.HTTP_400_BAD_REQUEST)
        tea_cont = controllers.TeacherController()
        user_val = tea_cont.create_teacher(username,email,password1,password2)   
        return response.Response({
                "msg": "user created",
                "result": True,
                "username": user_val.username,
               }
            )
    
    def get(self,request):
        user = request.user
        if not (user.is_superuser):
            return response.Response({
                "msg":"user permission is not allowed",
                "result":"false"
            }, status=status.HTTP_400_BAD_REQUEST)
        tea_cont = controllers.TeacherController()
        teacher_list = tea_cont.get_teacher()
        tea_list = serialisers.TeacherSerializer(teacher_list, many=True)
        return response.Response({
                "data": tea_list.data,
                "result": True,
               }
            )

    def put(self,pk):
        user = request.user
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')
        if not (user.is_superuser):
            return response.Response({
                "msg":"user permission is not allowed",
                "result":"false"
            }, status=status.HTTP_400_BAD_REQUEST)
        tea_cont = controllers.TeacherController()
        upd_teacher = tea_cont.update_teacher(username, email, password1, password2, pk)
        return response.Response({
                "username": upd_teacher.username,
                "msg":"Data updated sucessfully",
                "result": True,
               }
            )

    def delete(self,request,pk):
        user = request.user
        if not (user.is_superuser):
            return response.Response({
                "msg":"user permission is not allowed",
                "result":"false"
            }, status=status.HTTP_400_BAD_REQUEST)
        tea_cont = controllers.TeacherController()
        del_teacher = tea_cont.delete_teacher(pk)
        return response.Response({
            "msg":"teacher deleted sucessfully"
        })

class AssignSubject(views.APIView):

    def put(self,request):  
        user = request.user
        data = request.data
        teachers_id = data.get('teacher id')
        standard_id = data.get('subject id')
        if not (user.is_superuser):
            return response.Response({
                    "msg":"user permission is not allowed",
                    "result":"false"
                }, status=status.HTTP_400_BAD_REQUEST)
        tea_assign = controllers.AddSubjectToTeacher()
        tea_assign.add_subject_to_teacher(teachers_id, standard_id)
        return response.Response({
            "msg":"added sucessfully",
        })




