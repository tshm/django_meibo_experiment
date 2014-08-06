from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('meibos.urls')),
    url(r'^meibo/', include('meibos.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
