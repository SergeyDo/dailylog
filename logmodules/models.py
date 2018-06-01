# -*- coding: utf-8 -*-

from django.db import models, connection
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
import datetime

from django.conf import settings
User = settings.AUTH_USER_MODEL

class Log(models.Model):
    author = models.ForeignKey('auth.User', blank=True, null=True,  on_delete=models.CASCADE, related_name='aaa')
    line = models.TextField(blank=True, null=True, )
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    event_time = models.TimeField(default=datetime.datetime.now().strftime("%H:%M"))
    event_date = models.DateField(auto_now=True)
    username = models.CharField(max_length=90)

    def save(self):
        super(Log, self).save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.line

    def get_absolute_url(self):
        return reverse('logmodules:list')


