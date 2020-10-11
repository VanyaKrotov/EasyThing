from Service.serializers import ServiceGetSerializer
from Company.models import Company, CompanyNews
from User.serializers import UserNameSerializer
from rest_framework import serializers
import json


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyNewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyNews
        fields = '__all__'


class CompanyNewsGetSerializer(serializers.ModelSerializer):
    author = UserNameSerializer()

    class Meta:
        model = CompanyNews
        fields = ('id', 'title', 'article', 'likes',
                  'dateCreate', 'permissions', 'author')


class CompanyGetSerializer(serializers.ModelSerializer):
    news = CompanyNewsGetSerializer(many=True)
    location = serializers.SerializerMethodField()
    services = ServiceGetSerializer(many=True)

    class Meta:
        model = Company
        fields = ('id', 'master', 'title', 'email', 'dateCreated', 'logo', 'services',
                  'dateRegistration', 'description', 'location', 'news')

    def get_location(self, obj):
        return json.loads(obj.location)
