
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from python_http_client.exceptions import handle_error

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
                  path('accounts/', include('accounts.urls')),
                  path("ckeditor5/", include('django_ckeditor_5.urls')),

                  path("candidates/", include("candidates.urls", namespace="candidates")),
                  path('documents/', include('manage_documents.urls')),
                  path('jobs/', include('jobs.urls', namespace='jobs')),

              ] + debug_toolbar_urls()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


