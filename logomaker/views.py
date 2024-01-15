from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import (
    Logo_Category,
    )
from django.views.generic import (
    ListView,
    DetailView
)
from django.shortcuts import get_object_or_404

class LogoMakerIndexView(ListView):
    template_name = "logomaker/index.html"
    model = Logo_Category

    def get_queryset(self):
        return super().get_queryset().all().values_list("category_name", "category_slug")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = self.get_queryset()
        return context
    
    

class CategoryDetailView(DetailView):
    model = Logo_Category
    template_name = "logomaker/category_detail.html"
    pk_url_kwarg = "logo_category"

    def get_queryset(self):
        category_passed = self.kwargs.get("logo_category")
        qset = get_object_or_404(self.model, category_slug=category_passed)
        return super().get_queryset()
            
