from django.urls import path
from . import views

app_name = 'formsandbox'

urlpatterns = [
    path('', views.LoginView, name='login'),
]
