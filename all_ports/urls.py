from django.urls import path
from . import views

urlpatterns = [
    path('all-ports/', views.entryPage, name='allPorts'),
]
