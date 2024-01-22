from django.shortcuts import render
from django.views.generic import TemplateView




class HomePageView(TemplateView):
    template_name = "homepage.html"


class PagesView(TemplateView):
    template_name = "pages/about.html"
