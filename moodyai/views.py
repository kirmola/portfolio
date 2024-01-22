from django.shortcuts import render
from django.views.generic import TemplateView


class MoodyIndexView(TemplateView):
    template_name = "moodyai/index.html"
