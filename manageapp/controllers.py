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
        
             

