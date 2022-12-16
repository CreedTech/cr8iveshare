from django.urls import path
from .views import (
    index,
    about,
    contact,
)
from accounts.views import *

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    # path('signup', signup, name='signup'),
    # path('signin', signin, name='signin'),
    # path('logout', logout, name='logout'),
    # path('register/', RegisterView.as_view(), name='register'),
]
