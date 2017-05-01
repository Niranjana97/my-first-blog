# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Personal(models.Model):
    author = models.ForeignKey('auth.User', default='')
    name = models.CharField(max_length=30,default='')
    rollno = models.IntegerField(default=0)
    cgpa = models.FloatField(default=0.0)
    email = models.EmailField(default='')

    def __str__(self):
        return self.name

