from .serializers import CompanyDetailSerializer, CompanyNewsDetailSerializer, CompanyNewsGetSerializer, CompanyGetSerializer
from rest_framework.authentication import BasicAuthentication
from User.serializers import CsrfExemptSessionAuthentication
from rest_framework.permissions import IsAuthenticated
from Service.serializers import ServiceGetSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, CompanyNews
from django.contrib.auth.models import User
from rest_framework import generics
from django.shortcuts import render
from Service.models import Service
from django.core.exceptions import ObjectDoesNotExist


class CompanyCreateView(generics.CreateAPIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    serializer_class = CompanyDetailSerializer


class CompanyDeleteView(generics.DestroyAPIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()
    lookup_field = 'id'


class CompanyEditView(generics.UpdateAPIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()
    lookup_field = 'id'


class CompanyCreateNewsView(generics.CreateAPIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    serializer_class = CompanyNewsDetailSerializer


class CompanyDeleteNewsView(generics.DestroyAPIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    serializer_class = CompanyNewsDetailSerializer
    queryset = CompanyNews.objects.all()
    lookup_field = 'id'


class CompanyEditNewsView(generics.UpdateAPIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    serializer_class = CompanyNewsDetailSerializer
    queryset = CompanyNews.objects.all()
    lookup_field = 'id'


class CompanyListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        companies = Company.objects.filter(master=request.user.id)
        serializer = CompanyGetSerializer(companies, many=True)

        return Response(serializer.data)


class CompanyView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, id):
        try:
            company = Company.objects.get(id=id)
            serializer = CompanyGetSerializer(company)

            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"detail": "Компания не найдена"}, status=404)


class CompanyNewsListView(APIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

    def get(self, request, companyId):
        companyNews = CompanyNews.objects.filter(company=companyId)
        serializer = CompanyNewsGetSerializer(companyNews, many=True)

        return Response(serializer.data)


class ChangeCompanyNewsLikeView(APIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

    def put(self, request, postId):
        try:
            post = CompanyNews.objects.get(id=postId)

            if post.likes.filter(id=request.user.id).count() == 0:
                post.likes.add(request.user)
            else:
                post.likes.remove(request.user)

            serializer = CompanyNewsGetSerializer(post)

            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"detail": "Пост не найден"}, status=404)
