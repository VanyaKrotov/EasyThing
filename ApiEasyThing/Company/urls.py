from Company.views import CompanyCreateView, CompaniesAllView, CompanyView, CompanyCreateNewsView, CompanyDeleteNewsView, CompanyEditNewsView
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

urlpatterns = [
    path('Create/', csrf_exempt(CompanyCreateView.as_view())),
    path('Companies/', CompaniesAllView.as_view()),
    path('<int:id>/', CompanyView.as_view()),
    path('News/Create/', CompanyCreateNewsView.as_view()),
    path('News/Edit/<int:id>/', CompanyEditNewsView.as_view()),
    path('News/Delete/<int:id>/', CompanyDeleteNewsView.as_view()),
]
