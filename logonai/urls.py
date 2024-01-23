from django.urls import path
from .views import (
    LogonIndexView,
)

urlpatterns = [
    path("", LogonIndexView.as_view(), name="logon_home")
]
