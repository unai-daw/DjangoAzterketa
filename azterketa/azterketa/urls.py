from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('Kotxeak/', include('Kotxeak.urls')),
    path('pertsonak/', include('pertsonak.urls')),
    path('admin/', admin.site.urls),
]
