from django.contrib import admin
from catalog.models import Product, Category
from catalog.forms import ProductAdminForm

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
	form = ProductAdminForm

	#sets values for how the admin lists your products
	list_display = ('name', 'price',)
	list_display_links = ('name',)
	list_per_page = 50
	ordering = ['-created_at']
	search_fields = ['name']
	exclude = ('created_at', 'update_at',)

	#sets up slug to be generated from name
	prepopulated_fields = {'slug' : ('name',)}

#register product model with admin site
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):

	#sets values for how the admin lists your products
	list_display = ('name',)
	list_display_links = ('name',)
	list_per_page = 20
	ordering = ['name']
	search_fields = ['name']
	exclude = ('created_at', 'update_at',)

	#sets up slug to be generated from name
	prepopulated_fields = {'slug' : ('name',)}

#register product model with admin site
admin.site.register(Category, CategoryAdmin)