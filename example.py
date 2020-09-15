from articles.models import Article, Hashtag, Membership
data_news = Article.objects.all()
all_tags = Hashtag.objects.all()
membership = Membership.objects.all()


for member in membership:
    print(f'{member.article} {member.hashtag} tag is - {member.main_tag}')


{% load color_el_table %}
{{el | color_el}}">{{el | safe}}