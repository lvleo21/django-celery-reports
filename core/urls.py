from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReportView.as_view(), name="report_view"),
]