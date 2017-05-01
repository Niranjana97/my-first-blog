# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post
from .models import Personal

from django.contrib import admin
admin.site.register(Post)
# Register your models here.
admin.site.register(Personal)
