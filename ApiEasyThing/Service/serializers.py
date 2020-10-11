from rest_framework import serializers
from Service.models import Service, WorkSchedule, ServiceType
import json
from .services import getWorkScheduleDateFromString


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


class WorkScheduleGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = '__all__'

    def to_representation(self, values):

        return {
            'id': values.id,
            'title': values.title,
            'monday': getWorkScheduleDateFromString(values.monday),
            'tuesday': getWorkScheduleDateFromString(values.tuesday),
            'wednesday': getWorkScheduleDateFromString(values.wednesday),
            'thursday': getWorkScheduleDateFromString(values.thursday),
            'friday': getWorkScheduleDateFromString(values.friday),
            'saturday': getWorkScheduleDateFromString(values.saturday),
            'sunday': getWorkScheduleDateFromString(values.sunday),
        }


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'


class ServiceGetSerializer(serializers.ModelSerializer):
    workSchedule = WorkScheduleGetSerializer()
    location = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ('id', 'image', 'email', 'description', 'title', 'location',
                  'dateCreated', 'dateRegistration', 'company', 'children', 'workSchedule', 'types')

    def get_location(self, objectSerialize):
        return json.loads(objectSerialize.location)
