
from django.db import models
# Register your models here.



from django.contrib import admin
from article.models import Article

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("title", "slug", "date_time")

admin.site.register(Article, ArticleAdmin)