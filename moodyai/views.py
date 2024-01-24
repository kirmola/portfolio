from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from moodyai.forms import PersonalityForm
import requests
from json import dumps
from django.http import JsonResponse
from portfolio.seoclass import SEOClass


class MoodyIndexView(TemplateView):
    template_name = "moodyai/index.html"

    tags = SEOClass(
        title= "Moody: Absolutely Free Customizable AI Chatbot",
        description= "Moody is a free AI chatbot, fine tuned by you. Just enter your prompt, select mood, select tone, and you will get exact response from it, no signup required.",
        keywords= "Moody, AI, AI Chatbot, Free AI Chatbot, No signup",
    )


    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["form"] = PersonalityForm()
        context["meta_tags"] = self.tags.get_meta_tags()
        context["og_tags"] = self.tags.get_open_graph_tags()
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
