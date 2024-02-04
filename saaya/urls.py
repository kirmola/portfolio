from django.urls import path
from . import views

urlpatterns = [
    path('', views.saayaIndex, name='saaya_home'),
    path('results/', views.getResults, name='getresults')
]
