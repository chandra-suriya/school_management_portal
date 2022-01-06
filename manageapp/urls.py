from django.urls import path
from manageapp import views

urlpatterns = [
    path('createstandard/<int:pk>', views.StandardView().as_view(),name='createstandard'),
]