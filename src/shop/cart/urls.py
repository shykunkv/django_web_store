from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', 'cart.views.show_cart', {'template_name' : 'cart.html'}, name = "cart"),
    url(r'^checkout/$', 'cart.views.checkout', {'template_name' : 'checkout.html'}, name = "checkout"),
    url(r'^checkout_error/$', 'cart.views.checkout_error', {'template_name' : 'checkout_error.html'}, name = "checkout_error"),
]