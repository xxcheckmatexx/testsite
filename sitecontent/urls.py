from django.conf.urls import patterns, url

from sitecontent import views

urlpatterns = patterns('',
    url(r'^(?P<slug>[\w-]+)/$', views.index, name='contentPage')
)