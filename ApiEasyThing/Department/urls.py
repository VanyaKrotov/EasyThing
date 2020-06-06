from django.conf.urls import include
from django.urls import path
from Department.views import CreateDepartmentApiView, GetNowActiveDepartmentApiView

urlpatterns = [
    path('Registration/', CreateDepartmentApiView.as_view()),
    path('Get/<int:companyId>/<int:serviceId>/', GetNowActiveDepartmentApiView.as_view()),
]
