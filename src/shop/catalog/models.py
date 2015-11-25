from django.db import models

# Create your models here.

#class that represent Category
class Category(models.Model):
	name = models.CharField(max_length = 50)
	r_name = models.CharField(max_length = 50)
	#link
	slug = models.SlugField(max_length = 50, unique = True, help_text = 'unique value for product page URL, created from name')
	description = models.TextField()
	r_description = models.TextField()
	is_active = models.BooleanField(default = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __unicode__ (self):
		return self.name

	@models.permalink #method that generate links
	def get_absolute_url(self):
		return ('category', (), {'category_slug' : self.slug}) #template for link for category





#class that represent Product
class Product(models.Model):
	name = models.CharField(max_length = 255, unique = True)
	slug = models.SlugField(max_length = 255, unique = True, help_text = "unique value for product page URL, created from name.")
	brand = models.CharField(max_length = 50)
	price = models.DecimalField(max_digits = 9, decimal_places = 2)
	is_active = models.BooleanField(default = True)
	is_bestseller = models.BooleanField(default = False)
	quantity = models.IntegerField()
	description = models.TextField()
	r_description = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	categories = models.ManyToManyField(Category)

	image = models.ImageField(upload_to = 'images/products/main')
	thumbnail = models.ImageField(upload_to = 'images/products/thumbnails')
	image_caption = models.CharField(max_length = 200)

	def __unicode__ (self):
		return self.name

	@models.permalink #method that generate links
	def get_absolute_url(self):
		return ('product', (), {'product_slug' : self.slug}) #template for link for category
	