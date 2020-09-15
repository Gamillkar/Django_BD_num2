from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Hashtag, Membership


class HashtagInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            form.cleaned_data
            # raise ValidationError('Тут всегда ошибка')
        return super().clean()

class HashtagInline(admin.TabularInline):
    model = Membership
    formset = HashtagInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [HashtagInline]

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    inlines = [HashtagInline]