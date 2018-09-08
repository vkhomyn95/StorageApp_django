# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from place.models import Country, City

admin.site.register(Country)
admin.site.register(City)