from django.db import models

# Create your models here.
from django.urls import reverse

from users.models import CustomUser


class Committee(models.Model):
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, verbose_name='Committee Name')
    descriptions = models.TextField(max_length=1000)
    leaderNumber = models.IntegerField(null=False, verbose_name='Leader Number')
    memberNumber = models.IntegerField(null=False, verbose_name='Member Number')
    created_On = models.DateTimeField(auto_now_add=True)
    updated_On = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_On']

    def __str__(self):
        return self.name


class SlideView(models.Model):
    title = models.CharField(max_length=20, verbose_name='Title')
    description = models.CharField(max_length=100, verbose_name='Description')
    image = models.ImageField(upload_to='committee_photo', null=True, blank=True, verbose_name='Select Image')
    committee = models.ForeignKey(
        Committee,
        on_delete=models.CASCADE,
        related_name='committee',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('committee_detail')


class Leader(models.Model):
    committee = models.ForeignKey(
        Committee,
        on_delete=models.CASCADE
    )
    teacher = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.teacher.username


class Member(models.Model):
    committee = models.ForeignKey(
        Committee,
        on_delete=models.CASCADE
    )
    teacher = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.teacher.username
