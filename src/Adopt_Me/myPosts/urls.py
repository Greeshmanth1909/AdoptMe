from django.urls import path, include
from .views import my_post_view, edit_view

urlpatterns = [
    path('my posts/', my_post_view),
    path('<int:post_id>/edit/', edit_view, name='edit')
]