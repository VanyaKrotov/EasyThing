from django.conf.urls import include
from django.urls import path
from Workers.views import RegistrationWorkerApiView

urlpatterns = [
    path('Registration/', RegistrationWorkerApiView.as_view())
]
