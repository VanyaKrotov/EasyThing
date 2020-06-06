from Service.views import CreateServiceView, ServiceListView
from django.urls import path

urlpatterns = [
    path('Create/', CreateServiceView.as_view()),
    path('GetListByCompanyId/<int:id>/', ServiceListView.as_view())
]
