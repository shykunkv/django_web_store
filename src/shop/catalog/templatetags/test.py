from django import template

register = template.Library()

@register.assignment_tag
def get_lang():
	lang = 'en-us'
	if 'lang' in request.session:
		lang = request.session['lang']
	return lang