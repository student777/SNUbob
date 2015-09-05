from django.db import models
from bobshow.utils import random_name_upload_to, thumbnail
from django.db.models.signals import pre_save
from django.core.files import File
from django.conf import settings


class Bob(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to=random_name_upload_to)
    content = models.TextField(blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    place = models.ForeignKey('Place')
    star = models.PositiveSmallIntegerField()
    score = models.FloatField()


    def __str__(self):
        return self.name

    def cal_mean(self):
        n = self.comment_set.count() + 1
        a = self.star
        for i in self.comment_set.all():
            a = a + i.star
        score = a/n
        self.score = round(float(score), 2)
        self.save()


class Place(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Photo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    image = models.ImageField(blank=True, null=True, upload_to=random_name_upload_to)
    bob = models.ForeignKey(Bob)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    bob = models.ForeignKey(Bob)
    star = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + self.content

    class Meta:
        ordering = ('-pk', )


def pre_on_post_save(sender, **kargs):
    post = kargs['instance']
    if post.image:
        max_width = 300
        if post.image.width > max_width or post.image.height > max_width:
            processed_file = thumbnail(post.image.file, max_width, max_width)
            post.image.save(post.image.name, File(processed_file))

pre_save.connect(pre_on_post_save, sender=Bob)
