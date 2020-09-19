from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    data_news = Article.objects.all()
    context = {'object_list': data_news, }
    return render(request, template, context)

