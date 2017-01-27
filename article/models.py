from django.db import models

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True)
    shortDes = models.CharField(blank=True, max_length=500)
    date_time = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)


    def __str__(self) :
        return self.title

    class Meta:
        ordering = ['-date_time']


from draceditor.models import DraceditorField

class Post(models.Model):
    description = DraceditorField()