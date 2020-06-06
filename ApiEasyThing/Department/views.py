from django.shortcuts import render
from User.serializers import CsrfExemptSessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from Department.serializers import DepartmentSerializers, GetDepartmentSerializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from Department.models import Department


class CreateDepartmentApiView(generics.CreateAPIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = DepartmentSerializers
    permission_classes = (IsAuthenticated, )


class GetNowActiveDepartmentApiView(generics.ListAPIView):
    def get(self, request, companyId, serviceId):
        queryset = Department.objects.all()

        departments = GetDepartmentSerializers(queryset.filter(
            service=serviceId) if serviceId else queryset.filter(company=companyId), many=True).data

        return Response({"departments": departments})

    permission_classes = (IsAuthenticated, )
