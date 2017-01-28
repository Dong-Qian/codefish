
from django.db import models
# Register your models here.



from django.contrib import admin

from draceditor.widgets import AdminDraceditorWidget

from article.models import Article



class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminDraceditorWidget},
    }
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)