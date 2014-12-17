from django.conf.urls import patterns, url

from product import views

urlpatterns = patterns('',
	url(r'^$', views.product, name='productPage'),
    url(r'^(?P<slug>[\w-]+)/$', views.productFinal, name='product'),

)