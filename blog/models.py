from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default='')

    def get_truncated(self):
        return self.body[:200] + ' ...'

    def __str__(self):
        return self.title[:100]

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
