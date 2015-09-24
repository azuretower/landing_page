from django.db import models
from django.contrib.auth.models import User
from markupfield.fields import MarkupField

# https://github.com/jamesturk/django-markupfield

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    text = MarkupField(markup_type='markdown', null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField(default=True)
    # featured_image = models.ImageField(upload_to='image_uploads', null=True, blank=True)

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    post = models.ManyToManyField('Post')

    def __unicode__(self):
        return self.name
