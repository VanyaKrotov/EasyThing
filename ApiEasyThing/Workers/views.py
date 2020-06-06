from rest_framework import generics
from rest_framework.response import Response
from User.serializers import CsrfExemptSessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from Workers.serializers import WorkHistorySerializers


class RegistrationWorkerApiView(generics.CreateAPIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = WorkHistorySerializers
    permission_classes = (IsAuthenticated, )

# class GetHistoryWorkersApiView(generics.ListAPIView):
#     authentication_classes = (
#         CsrfExemptSessionAuthentication, BasicAuthentication)
#     permission_classes = (IsAuthenticated, )
#     serializer_class = 
