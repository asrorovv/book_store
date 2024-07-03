

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
