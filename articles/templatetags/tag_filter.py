import operator

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

    sorted_all_tag = sorted(temp_tag_dict.items(), key=operator.itemgetter(1), reverse=True)
    result_tag = []
    for tag in sorted_all_tag:
        sorted_list_tag = list(tag)[0]
        result_tag.append(sorted_list_tag)
    return result_tag
