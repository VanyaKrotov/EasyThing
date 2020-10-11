from django.contrib import admin
from Service.models import Service, ServiceType, WorkSchedule

admin.site.register(Service)
admin.site.register(ServiceType)
admin.site.register(WorkSchedule)
