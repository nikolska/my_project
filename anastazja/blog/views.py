from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Article, Comment
from django.urls import reverse
from django.shortcuts import get_object_or_404

def inblog(request):
	latest_articles_list = Article.objects.order_by('-pub_date')[:10]
	return render(request, 'blog/blog.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
	except:
		raise Http404('Статья не найдена!')
	latest_comments_list = a.comment_set.order_by('-id')[:10]
	return render(request, 'blog/blog_detail.html', {'article' : a, 'latest_comments_list': latest_comments_list})

def leave_comment(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
	except:
		raise Http404('Статья не найдена!')
	a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])
	return HttpResponseRedirect(reverse('blog:detail', args=(a.id,)))

def add_like(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
		article = get_object_or_404(Article, id = article_id)
		article.likes += 1
		article.save()
	except:
		return Http404('Ошибка')
	return HttpResponseRedirect(reverse('blog:detail', args=(a.id,)))


def add_dislike(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
		article = get_object_or_404(Article, id = article_id)
		article.dislikes += 1
		article.save()
	except:
		return Http404('Ошибка')
	return HttpResponseRedirect(reverse('blog:detail', args=(a.id,)))
