from typing import Any
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import PersonalityForm
from django.views.generic.edit import FormView
from .logics import GenerateResponse
# Create your views here.

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

    async def get(self, request):
        return await render(request, "moodyai/index.html")
    
    async def generate_response(self, query, mood_style, language_style):
        instance = GenerateResponse()
        return await instance.generate_response(query=query, mood_style=mood_style, language_style=language_style)

    async def post(self,request):
        post_data = request.POST
        mood_style = post_data.get("mood_style")
        language_style = post_data.get("language_style")
        query = post_data.get("query")
        

        api_response = await self.generate_response(query=query, mood_style=mood_style, language_style=language_style)
        if api_response["success"] is True:
            main_response = api_response["result"]["response"]
            return HttpResponse(
            f'''            
            <p>{main_response}</p>
            '''
        )

        else:
            error = api_response['errors'][0]['message']
            main_response = f"Something is not in correct place. Please Report this problem. Problem is: {error}"
            return HttpResponse(
            f'''            
            <p>{main_response}</p>
            '''
        )

