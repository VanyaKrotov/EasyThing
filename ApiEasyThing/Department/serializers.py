from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import serializers
from Department.models import Department
from Position.serializers import GetPositionSerializers


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class GetDepartmentSerializers(serializers.ModelSerializer):
    positions = GetPositionSerializers(many=True)

    class Meta:
        model = Department
        fields = ('title', 'description', 'positions')
