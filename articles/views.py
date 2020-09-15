from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Hashtag, Membership


def articles_list(request):
    template = 'articles/news.html'
    data_news = Article.objects.all()
    all_tags = Hashtag.objects.all()
    membership = Membership.objects.all()
    temp_tag_dict = {}
    for title in data_news:
        for member in membership:
            if str(title.title) == str(member.article):
                temp_tag_dict[str(member.hashtag)] = str(member.main_tag)
    list(temp_tag_dict).sort(key=lambda i: i[1])
    temp_tag_list = []
    for tag in temp_tag_dict:
        temp_tag_list.append(tag)
                # print(f'{title.title} {member.hashtag} tag is - {member.main_tag}')


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    context = {'object_list': data_news,
               'tags': all_tags}
    return render(request, template, context)

