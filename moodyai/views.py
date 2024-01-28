from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from moodyai.forms import PersonalityForm
import requests
from json import dumps
from django.http import HttpRequest, StreamingHttpResponse


class MoodyIndexView(TemplateView):
    template_name = "moodyai/index.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["form"] = PersonalityForm()
        return context


class GenerateResponseView(TemplateView):

    template_name = "moodyai/response.html"
    content_type = "text/event-stream"

    def generate_response(self, query, mood_style, language_style):
        API_BASE_URL = "https://moody.amanrawat.workers.dev/"
        inputs = {
            "query": query,
            "mood_style": mood_style,
            "language_style": language_style
        }
        with requests.post(API_BASE_URL, json=inputs, stream=True) as response:
            for chunk in response.iter_content(chunk_size=1):
                yield chunk

    def get(self, request):
        query = self.request.GET.get("query")
        mood_style = self.request.GET.get("mood_style")
        language_style = self.request.GET.get("language_style")
        response = self.generate_response(query, mood_style, language_style)
        return StreamingHttpResponse(response, headers = {
            "content-type":"text/event-stream"
        })     
