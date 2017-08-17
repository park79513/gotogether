from django.db import models
from django.db import models
from django.utils import timezone

from django.db.models.signals import pre_save, post_save

from django.conf import settings


from .utils import unique_slug_generator

class Posts(models.Model):
    author       = models.ForeignKey('auth.User')
    name         = models.CharField(max_length=200)
    location     = models.CharField(max_length=120, null=True, blank=True)
    category     = models.CharField(max_length=120, null=True, blank=True)
    timestamp    = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)
    slug         = models.SlugField(null=True, blank=True)
    text         = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()

pre_save.connect(rl_pre_save_receiver, sender=Posts)
# Create your models here.
