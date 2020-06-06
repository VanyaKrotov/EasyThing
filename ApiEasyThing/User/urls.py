from django.urls import path, include
from User.views import *

urlpatterns = [
    path('Create/', UserCreateView.as_view()),
    path('Create/Profile/', ProfileCreateView.as_view()),
    path('All/', UserListView.as_view()),
    path('Login/', LoginView.as_view()),
    path('Logout/', LogoutView.as_view()),
    path('Auth/', AuthView.as_view())
]
