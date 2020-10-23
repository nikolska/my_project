from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product

admin.site.site_title = 'Административная панель'
admin.site.site_header = 'Административная панель'


class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'price', 'get_image',)
	readonly_fields = ("get_image",)
	
	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="150" height="150">')

	get_image.short_description = 'Изображение'

admin.site.register(Product, ProductAdmin)
