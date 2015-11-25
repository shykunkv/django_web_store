from django.core import urlresolvers
from django.http import HttpResponseRedirect
from catalog.forms import ProductAddToCartForm


from django.shortcuts import render_to_response, get_object_or_404
from catalog.models import Category, Product
from django.template import RequestContext
from cart import mycart

# Create your views here.

def index(request, template_name = "index.html"):
	page_title = "Django Web Store"
	if 'lang' not in request.session:
		request.session['lang'] = 'en-us'
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))

def ru(request, template_name = "index.html"):
	request.session['lang'] = 'ru'
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))

def en(request, template_name = "index.html"):
	request.session['lang'] = 'en-us'
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))


def show_category(request, category_slug, template_name = "category.html"):
	c = get_object_or_404(Category, slug = category_slug)
	products = c.product_set.all()
	page_title = c.name	
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))


def show_product(request, product_slug, template_name = "product.html"):
	p = get_object_or_404(Product, slug = product_slug)
	categories = p.categories.filter(is_active = True)
	page_title = p.name	
	
	if request.method == 'POST':
		# add to cart
		postdata = request.POST.copy()
		form = ProductAddToCartForm(request, postdata)

		# check if posted data is valid
		if form.is_valid():
			# add to cart and redirect to cart page
			mycart.add_to_cart(request)

			#if test cookie worked, get rid of it
			if request.session.test_cookie_worked():
				request.session.delete_test_cookie()
			url  = urlresolvers.reverse('cart')
			return HttpResponseRedirect(url)

	else:
		#it's a GET
		form = ProductAddToCartForm(request = request, label_suffix = ':')

	#assign the hidden input the product slug
	form.fields['product_slug'].widget.attrs['value'] = product_slug

	# set teh test cookie on our first GET request
	request.session.set_test_cookie()

	return render_to_response(template_name, locals(), context_instance = RequestContext(request))
 