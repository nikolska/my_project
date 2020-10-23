from django.db import models

class Product(models.Model):
	title = models.CharField('Название', max_length=100)
	description = models.TextField('Описание')
	price = models.PositiveIntegerField('Цена в $', default=0)
	image = models.ImageField('Изображение', upload_to='media/services/', default='pictures')

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = 'Услуга/товар'
		verbose_name_plural = 'Услуги/товары'
