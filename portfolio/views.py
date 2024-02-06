from django.shortcuts import render
from django.views.generic import TemplateView
from .seoclass import SEOClass



class HomePageView(TemplateView):
    template_name = "homepage.html"
    
    tags = SEOClass(
        title= "Welcome to Aman's Portfolio.",
        description= "Hi, I am Aman, (Kirmola) and this is my portfolio, just explore and give me some feedback though.",
        keywords= "Aman Rawat, kirmola, kirmola.dev, Portfolio",
    )

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["meta_tags"] = self.tags.get_meta_tags()
        context["og_tags"] = self.tags.get_open_graph_tags()
        return context
    



class PagesView(TemplateView):
    template_name = "pages/about.html"
