from django.conf.urls import patterns, url

from sitecontent import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)