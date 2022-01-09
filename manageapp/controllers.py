from manageapp import models
from rest_framework import serializers
class StandardController:

    def create_standard(self,standard: str):
        stand = models.Standard.objects.create(name=standard)
        return stand.id
    def get_standard(self):
        stand = models.Standard.objects.all()
        if not (stand):
             raise serializers.ValidationError(
                {"result": False, "msg": "No values are found"},
                code="validation_error",
                )
        return stand
    def update_standard(self,pk: int,standard: str):
        upd_stand = models.Standard.objects.get(id=pk)
        upd_stand.name = standard
        upd_stand.save()
        return upd_stand.name
    def delete_standard(self,pk: int,standard: str):
        upd_stand = models.Standard.objects.get(id=pk)
        upd_stand.delete()
        
class SubjectController:

    def create_subject(self,subject: str):
        stand = models.Subject.objects.create(name=subject)
        return stand.id
    def get_subject(self):
        stand = models.Subject.objects.all()
        if not (stand):
             raise serializers.ValidationError(
                {"result": False, "msg": "No values are found"},
                code="validation_error",
                )
        return stand
    def update_subject(self,pk: int,subject: str):
        upd_stand = models.Subject.objects.get(id=pk)
        upd_stand.name = subject
        upd_stand.save()
        return upd_stand.name
    def delete_subject(self,pk: int,subject: str):
        upd_stand = models.Subject.objects.get(id=pk)
        upd_stand.delete()

class TeacherController:

    def create_teacher(self,username: str,email: str,password1: str,
                       password2: str):
        user = User.objects.create(username=username,
                                        email=email,is_active=True)
        user.set_password(password1)
        user.is_staff = True
        user.save()
        token = Token.objects.get_or_create(user=user)[0] 
        models.Teacher.objects.create(name=user)
        return user

    def get_teacher(self):
        if(models.Teacher.objects.count()>0):
            tea_data = models.Teacher.objects.all()
        else:
            raise serializers.ValidationError(
                {"result": False, "msg": "No teachers are found"},
                code="validation_error",
                )
        return tea_data

    def update_teacher(self,username: str,email: str,password1: str,
                       password2: str,pk: int):
        user = User.objects.get(id=pk)
        user.username = username
        user.email = email
        user.set_password(password1)
        user.save()
        return user   
                     
    def delete_teacher(self,pk):
        user = User.objects.get(id=pk)
        tea_model=models.Teacher.objects.get(user=user)
        tea_model.delete()
        user.delete()

class AddSubjectToTeacher:

    def add_subject_to_teacher(self,teachers_id: int,subject_id: int):
        sub_obj = models.Subject.objects.get(id=subject_id)
        tea_obj = models.Teacher.objects.get(id=teachers_id)
        if(tea_obj.subject_name != None):
            raise serializers.ValidationError(
                {"result": False, "msg": "the name which you selected already has subject name "},
                code="validation_error",
                )
        if(models.Teacher.objects.filter(subject_name=sub_obj).exists()):
            raise serializers.ValidationError(
                {"result": False, "msg": "the subject with teacher is already exsists "},
                code="validation_error",
                )
        else:
            tea_obj.subject_name = sub_obj
            tea_obj.save()
            
    


