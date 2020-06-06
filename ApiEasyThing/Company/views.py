from .serializers import CompaniesDetailSerializer, CompanyDetailSerializer, CompanyNewsSerializer
from rest_framework.authentication import BasicAuthentication
from User.serializers import CsrfExemptSessionAuthentication
from rest_framework.permissions import IsAuthenticated
from Service.serializers import ServiceGetSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, CompanyNews
from rest_framework import generics
from django.shortcuts import render
from Service.models import Service


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


class CompaniesAllView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        companies = CompanyDetailSerializer(
            Company.objects.all().filter(master=request.user.id), many=True).data

        for company in companies:
            company["countServices"] = Service.objects.all().filter(
                company=company["id"]).count()

        return Response({"companies": companies})


class CompanyView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, id):
        company = CompaniesDetailSerializer(Company.objects.all().filter(
            id=id, master=request.user.id), many=True).data

        if not len(company):
            return Response({"detail": "Компания не найдена"}, status=404)

        company = company[0]

        company["services"] = ServiceGetSerializer(
            Service.objects.all().filter(company=id, parentService=None), many=True).data

        return Response({"company": company})


class CompanyCreateNewsView(generics.CreateAPIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    serializer_class = CompanyNewsSerializer


class CompanyDeleteNewsView(generics.DestroyAPIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    serializer_class = CompanyNewsSerializer
    queryset = CompanyNews.objects.all()
    lookup_field = 'id'


class CompanyEditNewsView(generics.UpdateAPIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    serializer_class = CompanyNewsSerializer
    queryset = CompanyNews.objects.all()
    lookup_field = 'id'
