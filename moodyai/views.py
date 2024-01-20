from typing import Any
from django.http.response import StreamingHttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import PersonalityForm
from .logics import generate_response


class MoodyAIIndexView(TemplateView):
    template_name = "moodyai/index.html"
    http_method_names = ["get", "post"]

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = PersonalityForm()
        return context


class ParseMoodForm(TemplateView):
    form_class = PersonalityForm
    template_name = "moodyai/index.html"

    def get(self, request):
        query = self.request.GET.get("query")
        mood_style = self.request.GET.get("mood_style")
        language_style = self.request.GET.get("language_style")
        response = generate_response(query, mood_style, language_style)
        return StreamingHttpResponse(response, headers={
            "content-type": "text/event-stream",
        })