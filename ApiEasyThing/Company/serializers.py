from Service.serializers import ServiceGetSerializer
from Company.models import Company, CompanyNews
from User.serializers import UserNameSerializer
from rest_framework import serializers


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyNews
        fields = '__all__'


class CompanyNewsGetSerializer(serializers.ModelSerializer):
    author = UserNameSerializer()

    class Meta:
        model = CompanyNews
        fields = ('id', 'title', 'article',
                  'dateCreate', 'permissions', 'author')


class CompaniesDetailSerializer(serializers.ModelSerializer):
    news = CompanyNewsGetSerializer(many=True)

    class Meta:
        model = Company
        fields = ('id', 'master', 'title', 'email', 'dateCreated',
                  'dateRegistration', 'description', 'location', 'news')
