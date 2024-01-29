from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from moodyai.forms import PersonalityForm
import requests
from json import dumps
from django.http import HttpRequest, StreamingHttpResponse
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
