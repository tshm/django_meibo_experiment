from django.conf.urls import patterns, url

from meibos import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
  url(r'^delete/(?P<pk>\d+)$', views.delete, name='delete'),
  url(r'^new$', views.new, name='detail'),
)
