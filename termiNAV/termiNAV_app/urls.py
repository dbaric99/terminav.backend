from django.urls import path
from . import views

app_name = "termiNAV"

urlpatterns = [
    path('', views.Index, name="index"),
]
