from django.urls import path
from .views import (
    MoodyIndexView,
    GenerateResponseView
)

urlpatterns = [
    path("", MoodyIndexView.as_view(), name="moody_home"),
    path("generate/", GenerateResponseView.as_view(), name="generate_response"),
]
