from django.db import models

# Create your models here.
from django.db.models import permalink
from django.template.defaultfilters import slugify


class Article(models.Model) :
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True)
    date_time = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.id:  # stackoverflow有人建议设置这个，让每篇文章的标题只slugify一次。
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)

    def __str__(self) :
        return self.title

    class Meta:
        ordering = ['-date_time']


