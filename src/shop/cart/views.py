from django.shortcuts import render_to_response
from django.template import RequestContext
import mycart
from django.core import urlresolvers
from django.http import HttpResponseRedirect

# Create your views here.

def show_cart(request, template_name = "cart.html"):
	if request.method == "POST":
		postdata = request.POST.copy()
		if postdata['submit'] == 'Remove':
			mycart.remove_from_cart(request)
		if postdata['submit'] == 'Update':
			mycart.update_cart(request)

	cart_items = mycart.get_cart_items(request)
	cart_subtotal = mycart.cart_subtotal(request)		
	page_title = 'Shipping Cart'
	
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))



def checkout(request, template_name = "index.html"):
	cur_user = request.user
	if cur_user.groups.filter(name = "black_list").exists():
		url  = urlresolvers.reverse('checkout_error')
		return HttpResponseRedirect(url)
	else:
		cart_items = mycart.get_cart_items(request)
		for item in cart_items:
			mycart.remove_from_cart_by_id(request, item.id)
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))


def checkout_error(request, template_name = "checkout_error.html"):
	
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))
