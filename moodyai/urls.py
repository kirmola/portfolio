from django.urls import path
from .views import MoodyAIIndexView

urlpatterns = [
    path("", MoodyAIIndexView.as_view(), name="moodyaiindex"),
    path("respond/", MoodyAIIndexView.as_view(), name="moodyairespond")
]
