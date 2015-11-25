from django.shortcuts import render


def home(request):
	context = {}
	template = "home.html"
	return render_to_response(template, locals(), context_instance = RequestContext(request))

def catalog(request):
	context = {}
	template = "catalog.html"
	return render(request, template, context)