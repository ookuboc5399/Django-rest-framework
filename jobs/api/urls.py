from django.urls import path
from jobs.api import views

urlspatterns = [
    path('jobs/', views.ListView.as_view(),name='list')
]