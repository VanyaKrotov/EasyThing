from User.serializers import UserDetailSerializer, UserGetSerializer, ProfileDetailSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from User.models import Profile


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer


class ProfileCreateView(generics.CreateAPIView):
    serializer_class = ProfileDetailSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserGetSerializer
    queryset = User.objects.all()

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None and user.is_active:
            login(request, user)
            userData = UserGetSerializer(User.objects.all().filter(
                username=request.user.username), many=True).data

            return Response({"user": userData[0]})
        else:
            return Response({"detail": "Имя пользователя или пароль не верны. Проверте корректность введенных данных."}, status=400)


class LogoutView(APIView):
    def get(self, request,):
        logout(request)
        return Response({"user": None})


class AuthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        userData = UserGetSerializer(User.objects.all().filter(
            username=request.user.username), many=True).data

        return Response({"user": userData[0]})
