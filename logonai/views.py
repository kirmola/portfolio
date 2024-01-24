from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import LogonForm
import requests
from django.http import FileResponse
from PIL import Image
from io import BytesIO
from django.core.files.temp import NamedTemporaryFile
from portfolio.seoclass import SEOClass

class LogonIndexView(TemplateView):
    template_name = "logonai/index.html"

    
    tags = SEOClass(
        title= "Logon: Truly Free AI Image Generator",
        description= "Here is the absolutely free AI image genertor. Just enter your query and you are good to go, no signup required.",
        keywords= "Logon, AI, AI Image Generator, Image Generator",
    )


    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["form"] = LogonForm()
        context["meta_tags"] = self.tags.get_meta_tags()
        context["og_tags"] = self.tags.get_open_graph_tags()
        return context


class GenerateImageView(TemplateView):

    def generate_response(self, prompt):
        API_BASE_URL = "https://logon.amanrawat.workers.dev/"
        inputs = {
            "prompt": prompt,
        }
        response = requests.post(API_BASE_URL, json=inputs)
        results = response.content
        return results

    def post(self, request):
        prompt = self.request.POST.get("prompt")
        response = self.generate_response(prompt)
        # image = Image.open(BytesIO(response))
        fname = f"{prompt}.png"
        with NamedTemporaryFile("wb", prefix=fname) as tempFile:      
            tempFile.write(response)
        out = FileResponse(filename=fname, headers={
            "content-type": "image/png",
        })
        return out
