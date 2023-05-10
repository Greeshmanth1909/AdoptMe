"""urls for upload"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('post/', views.upload_view)
]