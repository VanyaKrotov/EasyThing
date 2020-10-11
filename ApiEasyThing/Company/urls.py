from Company.views import CompanyCreateView, CompanyListView, CompanyView, CompanyCreateNewsView, CompanyDeleteNewsView, CompanyEditNewsView, CompanyDeleteView, CompanyEditView, CompanyNewsListView, ChangeCompanyNewsLikeView
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

urlpatterns = [
    path('Create/', csrf_exempt(CompanyCreateView.as_view())),
    path('Delete/<int:id>/', CompanyDeleteView.as_view()),
    path('Edit/<int:id>/', CompanyEditView.as_view()),
    path('Companies/', CompanyListView.as_view()),
    path('<int:id>/', CompanyView.as_view()),
    path('<int:companyId>/News/', CompanyNewsListView.as_view()),
    path('News/Create/', CompanyCreateNewsView.as_view()),
    path('News/Edit/<int:id>/', CompanyEditNewsView.as_view()),
    path('News/Delete/<int:id>/', CompanyDeleteNewsView.as_view()),
    path('News/<int:postId>/Likes/', ChangeCompanyNewsLikeView.as_view()),
]
