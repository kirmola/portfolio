# Async functions are suspeded until aiohttp is fixed for python 3.12

from django.utils.text import slugify
# import aiohttp, asyncio, boto3
import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import LogonForm
import requests
from django.http import HttpResponse
from portfolio.seoclass import SEOClass
from base64 import b64encode
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
    content_type = "image/png"
    template_name = "logonai/index.html"

    # async def generate_response(self, prompt):
    #     API_BASE_URL = "https://logon.amanrawat.workers.dev/"
    #     inputs = {
    #         "prompt": prompt,
    #     }
    #     async with aiohttp.ClientSession() as session:
    #         async with session.post(API_BASE_URL, json=inputs) as response:
    #             return await response.read()
    def generate_response(self, prompt):
        API_BASE_URL = "https://logon.amanrawat.workers.dev/"
        inputs = {
            "prompt": prompt,
        }
        # with aiohttp.ClientSession() as session:
        with requests.post(API_BASE_URL, json=inputs) as response:
            return response.content
            
    # async def upload_to_s3(self, filename, binary_data):
    #         s3 = boto3.resource('s3',
    #             endpoint_url=f'https://{environ.get("CF_ACCOUNT_ID")}.r2.cloudflarestorage.com',
    #             aws_access_key_id=environ.get("CF_ACCESS_KEY_ID"),
    #             aws_secret_access_key=environ.get("CF_SECRET_ACCESS_KEY")
    #         )
    #         s3.Bucket(environ["BUCKET_NAME"]).put_object(Key=filename, Body=binary_data, Metadata={
    #             "Content-Type": "image/png"
    #         })


    # async def process_image(self, prompt):
    def process_image(self, prompt):
        # data = await self.generate_response(prompt)
        data = self.generate_response(prompt)
        base64_image = b64encode(data).decode("utf-8")
        filename = f"{slugify(prompt)}.png"
        try:
            self.upload_to_s3(filename, data)
            # await self.upload_to_s3(filename, data)
        except:
            pass
        return f'<img src="data:image/png;base64,{base64_image}" alt="Result for {prompt}">'

    async def post(self, request):
        prompt = self.request.POST.get("prompt")
        # image_html = await self.process_image(prompt)
        image_html = self.process_image(prompt)
        return HttpResponse(image_html)

    async def get(self, requst):
        return render(requst, self.template_name)