from .serializers import ServiceDetailSerializer, ServiceListSerializer
from rest_framework.authentication import BasicAuthentication
from User.serializers import CsrfExemptSessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics
from django.shortcuts import render
from Service.models import Service

class CreateServiceView(generics.CreateAPIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    serializer_class = ServiceDetailSerializer


class ServiceListView(generics.ListAPIView):
	permission_classes = (IsAuthenticated, )
    
	def get(self, request, id):
		services = ServiceListSerializer(Service.objects.all().filter(company=id), many=True).data

		return Response({"services": services})
        
