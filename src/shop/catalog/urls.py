from django.conf.urls import *

urlpatterns = [
    url(r'^$', 'catalog.views.index', {'template_name' : 'index.html'}, name = "catalog"),
    url(r'^ru/', 'catalog.views.ru', {'template_name' : 'index.html'}, name = "ru"),
    url(r'^en/', 'catalog.views.en', {'template_name' : 'index.html'}, name = "en"),
    url(r'^category/(?P<category_slug>[-\w]+)/$', 'catalog.views.show_category', {'template_name' : 'category.html'}, 'category'),
    url(r'^product/(?P<product_slug>[-\w]+)/$',	'catalog.views.show_product', {'template_name' : 'product.html'}, 'product'),
]