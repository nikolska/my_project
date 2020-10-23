from django.db import models


class Phone(models.Model):
	phone = models.CharField('telephon', max_length=15)

	def __str__(self):
		return self.phone

	class Meta:
		verbose_name = 'Телефон'
		verbose_name_plural = 'Телефоны'

class Mail(models.Model):
	mail = models.CharField('mail', max_length=30)

	def __str__(self):
		return self.mail

	class Meta:
		verbose_name = 'Мейл'
		verbose_name_plural = 'Мейлы'

class Address(models.Model):
	address = models.CharField('address', max_length=100)

	def __str__(self):
		return self.address

	class Meta:
		verbose_name = 'Адресс'
		verbose_name_plural = 'Адресса'

