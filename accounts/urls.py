from django.urls import path
from .views import *
from accounts.views import *


urlpatterns = [
    path('', AccountHomeView.as_view(), name='account'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
