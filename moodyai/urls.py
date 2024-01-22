from django.urls import path
from .views import (
    MoodyIndexView
)

urlpatterns = [
    path("", MoodyIndexView.as_view(), name="moody_home")
]
