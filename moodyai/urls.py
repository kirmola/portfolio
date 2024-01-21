from django.urls import path
from .views import (
    MoodyAIIndexView,
    ParseMoodForm
)

urlpatterns = [
    path("", MoodyAIIndexView.as_view(), name="moodyaiindex"),
    path("generate/", ParseMoodForm.as_view(), name="parsemoodform"),
]
