from django.conf.urls import include, url
from django.contrib import admin


admin.site.site_header = 'Recursos Humanos'

urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'^recursos/', include('recursos.urls')),
]
