from django.db import models
from bobshow.utils import random_name_upload_to, square_image
from django.db.models.signals import pre_save
from django.core.files import File


class Bob(models.Model):
    name = models.CharField(max_length=255)
    date = models.ManyToManyField('Date')
    place = models.ForeignKey('Place')
    score = models.FloatField(default=0)

    def __str__(self):
        return self.place.name + '/' + self.name

    def cal_mean(self):
        n = self.comment_set.count()
        if not n:
            self.score = -1
        else:
            a = 0
            for i in self.comment_set.all():
                a = a + i.star
            score = a / n
            self.score = round(float(score), 2)
            self.save()


class Place(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to=random_name_upload_to)
    bob = models.ForeignKey(Bob)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL) # TODO: account management
    bob = models.ForeignKey(Bob)
    star = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + self.content

    class Meta:
        ordering = ('-pk',)


class Date(models.Model):
    time = models.DateField()
    # is_lunch = models.BooleanField(default=True) # TODO: seperate moring/lunch/night

    def __str__(self):
        return str(self.time)


def pre_on_post_save(sender, **kargs):
    post = kargs['instance']
    if post.image:
        max_width = 300
        if post.image.width > max_width or post.image.height > max_width:
            processed_file = square_image(post.image.file, max_width, max_width)
            post.image.save(post.image.name, File(processed_file))


pre_save.connect(pre_on_post_save, sender=Image)
