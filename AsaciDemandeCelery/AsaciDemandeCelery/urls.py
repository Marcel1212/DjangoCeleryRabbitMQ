from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prometheus/', include('django_prometheus.urls')),
    path('demande/', include('Demande.urls'))
]
