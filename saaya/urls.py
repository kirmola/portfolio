from django.urls import path
from . import views

urlpatterns = [
    path('', views.saayaIndex, name='index'),
    path('results/', views.getResults, name='getresults')
]
