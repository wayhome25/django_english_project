# study/models.py
from django.db import models


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, verbose_name='제목')
    origin = models.CharField(max_length=200,  blank=True, null=True, verbose_name='원본 URL')
    video_url = models.CharField(max_length=100, blank=True, null=True, verbose_name='YouTube 링크')
    video_key = models.CharField(max_length=12, null=True, blank=True)
    text = models.TextField(verbose_name='내용')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('study.Post')
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
