from rest_framework import serializers
from manageapp import models

class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Standard
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Subject
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Teacher
        fields = '__all__'