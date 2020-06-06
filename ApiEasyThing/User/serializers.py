from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import User
from rest_framework import serializers
from User.models import Profile


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'id')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('telephone', 'birthDate')


class UserGetSerializer(serializers.ModelSerializer):
    profile = ProfileGetSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'email', 'user_permissions', 'last_login',
                  'username', 'last_name', 'date_joined', 'is_staff', 'is_active', 'profile')


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return
