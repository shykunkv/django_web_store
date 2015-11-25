from catalog.models import Category


def shop(request):
	return {
		'active_categories' : Category.objects.filter(is_active = True),
		'site_name' : "DJANGO WEB STORE",
		'request' : request,
	}