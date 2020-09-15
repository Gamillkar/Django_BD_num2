from django.template import library
from articles.models import  Membership

register = library.Library()

@register.filter
def tag_present(value):
    membership = Membership.objects.all()
    temp_tag_dict = {}
    for member in membership:
        if str(value) == str(member.article):
            temp_tag_dict[str(member.hashtag)] = str(member.main_tag)
    list(temp_tag_dict).sort(key=lambda i: i[1])
    temp_tag_list = []
    for tag in temp_tag_dict:
        temp_tag_list.append(tag)
    return temp_tag_list



