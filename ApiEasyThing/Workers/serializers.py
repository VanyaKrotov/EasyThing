from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import serializers
from User.serializers import UserNameSerializer
from Workers.models import WorkHistory


class WorkHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = "__all__"


class GetWorkHistorySerializers(serializers.ModelSerializer):
    user = UserNameSerializer()

    class Meta:
        model = WorkHistory
        fields = ("user", "startDate", "endDate")
