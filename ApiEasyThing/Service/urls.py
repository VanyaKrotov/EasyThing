from Service.views import CreateServiceView, ServiceListView, ServiceView, ServiceTypeListView, WorkScheduleListView
from django.urls import path

urlpatterns = [
    path('Create/', CreateServiceView.as_view()),
    path('<int:serviceId>/', ServiceView.as_view()),
    path('AllTypes/', ServiceTypeListView.as_view()),
    path('CompanyServices/<int:id>/', ServiceListView.as_view()),
    path('WorkShedudles/', WorkScheduleListView.as_view())
]
