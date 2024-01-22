from django.shortcuts import render
from django.views.generic import TemplateView




class MoodyIndexView(TemplateView):
    template_name = "moodyai/index.html"



class HomePageView(TemplateView):
    template_name = "homepage.html"


class PagesView(TemplateView):
    template_name = "pages/about.html"
