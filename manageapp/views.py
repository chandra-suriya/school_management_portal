from django.shortcuts import render
from manageapp import models, controllers, serialisers
from rest_framework import views, permissions
from rest_framework import serializers, response, parsers
from django.core import validators
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
    




