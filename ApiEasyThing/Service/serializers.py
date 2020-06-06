from rest_framework import serializers
from Service.models import Service

class ServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title')

    def to_representation(self, value):
        return {
            "label": value.title,
            "value": value.id
        }

class ServiceGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'country', 'adress', 'description', 'title', 'typeId', 'company', 'children')

    def get_fields(self):
        fields = super(ServiceGetSerializer, self).get_fields()
        fields['children'] = ServiceGetSerializer(many=True)
        return fields
