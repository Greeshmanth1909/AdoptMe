from . import views
from django.urls import path

urlpatterns = [
    path('search/', views.feed_view)
]

