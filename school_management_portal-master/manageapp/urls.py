from django.urls import path
from manageapp import views

urlpatterns = [
    path('createstandard/', views.StandardView().as_view(),name='createstandard'),
    path('createstandard/<int:pk>', views.StandardView().as_view(),name='createstandard'),
    path('createsubject/', views.SubjectView().as_view(),name='createsubject'),
    path('createsubject/<int:pk>', views.SubjectView().as_view(),name='createsubject'),
    path('createteacher/',views.TeacherView().as_view(),name='createteacher'),
    path('assign_subject/',views.AssignSubject().as_view(),name='assign_subject')

]