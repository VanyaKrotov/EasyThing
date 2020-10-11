from .serializers import ServiceDetailSerializer, ServiceListSerializer, ServiceGetSerializer, ServiceTypeSerializer, WorkScheduleGetSerializer
from rest_framework.authentication import BasicAuthentication
from User.serializers import CsrfExemptSessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import render
from Service.models import Service, ServiceType, WorkSchedule
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


class CreateServiceView(generics.CreateAPIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    serializer_class = ServiceDetailSerializer


class ServiceListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, id):
        services = ServiceGetSerializer(
            Service.objects.all().filter(company=id), many=True).data

        return Response(services)


class ServiceView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, serviceId):
        try:
            service = Service.objects.get(id=serviceId)
            serializer = ServiceGetSerializer(service)

            return Response(serializer.data)

        except ObjectDoesNotExist:
            return Response({"detail": "Предприятие не найдено"}, status=404)


class ServiceTypeListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer


class WorkScheduleListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        workSchedules = WorkScheduleGetSerializer(WorkSchedule.objects.filter(
            Q(master=None) | Q(master=request.user.id)), many=True).data

        return Response(workSchedules)
