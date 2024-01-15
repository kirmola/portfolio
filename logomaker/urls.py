from django.urls import path
from .views import (
    LogoMakerIndexView,
    CategoryDetailView
)



urlpatterns = [
    path('', LogoMakerIndexView.as_view(), name="logomakerindex"),
    path('logo-by-<slug:logo_category>/', CategoryDetailView.as_view(), name="categorydetailview")
]
