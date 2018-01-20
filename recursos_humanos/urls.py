from django.conf.urls import include, url
from django.contrib import admin
from .views import LoaderIO


admin.site.site_header = 'Recursos Humanos'

urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'^recursos/', include('recursos.urls')),
    url(r'^loaderio-65e703fb3f6975d8db96b9c226cf3648/', LoaderIO.as_view(), name='loarderio'),
]
