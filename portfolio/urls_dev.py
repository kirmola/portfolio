from .urls import *

urlpatterns+=[
    path("__reload__/", include("django_browser_reload.urls")),
]