from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class LogonIndexView(TemplateView):
    template_name = "logonai/index.html"

