# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from shops.models import TypeOfStore, Store

admin.site.register(TypeOfStore)
admin.site.register(Store)

