from typing import Any
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import render
# Create your views here.


class MoodyAIIndexView(CreateView):
    template_name = "moodyai/index.html"
    http_method_names = ["get", "post"]

    def get_queryset(self):
        return super().get_queryset()

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)
