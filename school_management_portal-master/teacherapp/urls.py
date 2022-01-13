from django.urls import path
from teacherapp import views

urlpatterns = [
     path('teachersignin/',views.TeacherSignin().as_view(),name='teachersignin'),
     path('createstudent/',views.CreateStudent().as_view(),name='createstudent')
]