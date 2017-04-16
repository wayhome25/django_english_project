# study/models.py
from django.db import models
from django.conf import settings

def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return '{}/{}.{}'.format(instance.author.username, pid, extension)


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, verbose_name='제목')
    origin = models.CharField(max_length=200,  blank=True, null=True, verbose_name='원본 URL')
    video_url = models.CharField(max_length=100, blank=True, null=True, verbose_name='YouTube 링크')
    video_key = models.CharField(max_length=12, null=True, blank=True)
    video_time = models.IntegerField(null=True, blank=True)
    video_url2 = models.CharField(max_length=100, blank=True, null=True, verbose_name='YouTube 링크2')
    video_key2 = models.CharField(max_length=12, null=True, blank=True)
    video_time2 = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to = user_path, blank=True, verbose_name='이미지 추가', help_text='이미지를 추가할 수 있습니다. not required')
    cover_img = models.ImageField(upload_to = user_path, blank=True, verbose_name='커버 이미지', help_text='상단의 커버 이미지를 설정할 수 있습니다. not required')
    text = models.TextField(verbose_name='내용')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('study.Post', related_name='comments')
    author = models.ForeignKey('auth.User')
    text = models.TextField(verbose_name='')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text
