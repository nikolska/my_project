import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
	title = models.CharField('Название статьи', max_length=300)
	text = models.TextField('Текст статьи')
	likes = models.IntegerField('Like', default=0)
	dislikes = models.IntegerField('Dislike', default=0)
	image = models.ImageField('Изображение', upload_to='media/blog/')
	pub_date = models.DateTimeField('Дата публикации', auto_now=True)

	def __str__(self):
		return self.title

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	author_name = models.CharField('Автор комментария', max_length=50)
	comment_text = models.TextField('Текст комментария', max_length=500)
	pub_date = models.DateTimeField('Дата публикации', auto_now=True)

	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'