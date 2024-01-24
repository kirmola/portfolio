from django.urls import path
from .views import (
    LogonIndexView,
    GenerateImageView,
)

urlpatterns = [
    path("", LogonIndexView.as_view(), name="logon_home"),
    path("generate/", GenerateImageView.as_view(), name="generate_image"),
]
