from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="제목")
    text = models.TextField(verbose_name="줄거리")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    poster = models.CharField(max_length=400, blank=True, null=True, verbose_name="포스터")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

