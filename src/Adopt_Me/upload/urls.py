"""urls for upload"""

from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django. conf import settings

urlpatterns = [
    path('post/', views.upload_view)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
