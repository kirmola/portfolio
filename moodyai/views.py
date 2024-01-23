from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from moodyai.forms import PersonalityForm
import requests
from django.http import JsonResponse


class MoodyIndexView(TemplateView):
    template_name = "moodyai/index.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["form"] = PersonalityForm()
        return context


class GenerateResponseView(TemplateView):
    content_type = "text/event-stream"

    def generate_response(self, query, mood_style, language_style):
        API_BASE_URL = "https://moody.amanrawat.workers.dev/"
        inputs = {
            "query": query,
            "mood_style": mood_style,
            "language_style": language_style
        }
        try:
            with requests.post(API_BASE_URL, json=inputs) as response:
                return response.json()
        except:
            return {"result": "Something is horribly wrong! JK, report this though."}

    def post(self, request):
        query = self.request.POST.get("query")
        mood_style = self.request.POST.get("mood_style")
        language_style = self.request.POST.get("language_style")
        try:
            response = self.generate_response(query, mood_style, language_style)
            result = response["response"]
        except:
            result = response["error"]
        return JsonResponse(result, json_dumps_params={
            "ensure_ascii":False
        }, safe=False)
