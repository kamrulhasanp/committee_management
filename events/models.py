from django.db import models
from django.urls import reverse

from committee.models import Committee
from users.models import CustomUser


# Create your models here.
class Event(models.Model):
    eventName = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='event-photo/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE)
    committeeEvent = models.ForeignKey(
        Committee,
        on_delete=models.CASCADE,
        related_name='committeeEvent')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.eventName

    def get_absolute_url(self):
        return reverse('event_detail')

    @property
    def picture_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Post(models.Model):
    post = models.TextField(max_length=500)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(Event,
                              on_delete=models.CASCADE,
                              related_name='event')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return reverse('event_detail')
