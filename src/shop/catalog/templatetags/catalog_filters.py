from django import template
import locale

register = template.Library()

@register.filter
def currency(value):
	try:
		locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
	except:
		locale.setlocale(locale.LC_ALL, '')
	loc = locale.localeconv()
	return locale.currency(value, loc['currency_symbol'], grouping = True)


