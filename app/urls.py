from django.urls import path
from app import views

urlpatterns = [
    path('', views.Index.as_view(), name='index')
]
