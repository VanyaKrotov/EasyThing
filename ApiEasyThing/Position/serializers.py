from rest_framework import serializers
from Position.models import Position
from Workers.serializers import GetWorkHistorySerializers


class GetPositionSerializers(serializers.ModelSerializer):
    workers = GetWorkHistorySerializers(many=True)

    class Meta:
        model = Position
        fields = ('id', 'title', 'description', 'workers')
