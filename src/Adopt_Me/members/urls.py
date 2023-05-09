# urls.py

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # ... other URLs ...

    # Login and logout views
    # path('login/', views.login_view),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', views.registration_view, name='register')
]
