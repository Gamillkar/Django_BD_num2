import json

from django.core.management.base import BaseCommand
from articles.models import Article


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('articles.json', encoding='utf-8') as json_file:
            data_file = json.load(json_file)
            for item in data_file:
                Article.objects.create(
                    title=item['fields']['title'],
                    text=item['fields']['text'],
                    published_at=item['fields']['published_at'],
                    image=item['fields']['image'],
                )