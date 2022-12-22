from django.shortcuts import render
from django.views.generic import *


class ReportView(TemplateView):
    template_name="core/report.html"


