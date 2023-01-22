from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from books.views import landing_page
from users.views import BaseTemplate

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('users/', include('users.urls'), name='users'),
    path('books/', include('books.urls'), name='books'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls'), name='api'),
    path('admin/', admin.site.urls)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
