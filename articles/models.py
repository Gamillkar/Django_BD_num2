from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    name = models.CharField(max_length=35)
    members = models.ManyToManyField(Article,
                                     related_name='hashtag',
                                     through='Membership'
                                     )

    def __str__(self):
        return self.name

class Membership(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE, verbose_name='Раздел')
    main_tag = models.BooleanField(default=False, verbose_name='Основной')


    def __str__(self):
        return '{0}_{1}'.format(self.article, self.hashtag)
