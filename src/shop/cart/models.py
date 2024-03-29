from django.db import models
from catalog.models import Product
import decimal
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class CartItem(models.Model):
	cart_id = models.CharField(max_length = 50)
	date_added = models.DateTimeField(auto_now_add = True)
	quantity = models.IntegerField(default = 1)
	product = models.ForeignKey('catalog.Product', unique = False)
	user = models.ForeignKey(User, null = True)

	class Meta:
		db_table = 'cart_item'
		ordering = ['date_added']

	
	def total(self):
		return self.quantity * self.product.price

		
	def name(self):
		return self.product.name

		
	def price(self):
		return self.product.price

		
	def get_absolute_url(self):
		return self.product.get_absolute_url()

    
	def augment_quantity(self, quantity):
		self.quantity = self.quantity + int(quantity)
		self.save()





















