from django.db import models

# Create your models here.
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.urls import reverse


class Article(models.Model) :
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50)
    date_time = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)

    def __str__(self) :
        return self.title

    class Meta:
        ordering = ['-date_time']

    def get_absolute_url(self):
        return reverse('postDetail', kwargs={"slug": self.slug})



