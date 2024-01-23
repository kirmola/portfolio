from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from moodyai.forms import PersonalityForm
import requests
from json import dumps
from django.http import JsonResponse


class MoodyIndexView(TemplateView):
    template_name = "moodyai/index.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["form"] = PersonalityForm()
        return context


class GenerateResponseView(TemplateView):

    def generate_response(self, query, mood_style, language_style):
        API_BASE_URL = "https://moody.amanrawat.workers.dev/"
        inputs = {
            "query": query,
            "mood_style": mood_style,
            "language_style": language_style
        }
        response = requests.post(API_BASE_URL, json=inputs)
        results = response.json()
        return results

    def post(self, request):
        query = self.request.POST.get("query")
        mood_style = self.request.POST.get("mood_style")
        language_style = self.request.POST.get("language_style")
        response = self.generate_response(query, mood_style, language_style)
        result = response["response"].replace('\n', '<br>')
        return JsonResponse(result, json_dumps_params={
            "ensure_ascii": False
        }, safe=False)
