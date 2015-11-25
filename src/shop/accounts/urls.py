import settings
from django.conf.urls import *

urlpatterns = [
    url(r'^register/$', 'accounts.views.register', {'template_name' : 'register.html'}, name = "register"),
    url(r'^my_account/$', 'accounts.views.my_account', {'template_name' : 'my_account.html'}, 'my_account'),
    #url(r'^order_details/(?P<order_id>[-\w]+)/$', 'accounts.views.order_details', {'template_name' : 'order_details.html'}, 'order_details'),
    #url(r'^order_info/$', 'accounts.views.order_info', {'template_name' : 'order_info.html'}, 'order_info'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name' : 'login.html'}, 'login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name' : 'index.html'}, 'logout'),

]
