from django.db import models


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_truncated(self):
        return self.body[:200] + ' ...'

    def __str__(self):
        return self.title[:100]
