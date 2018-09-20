# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import validators
from django.db import models

# Create your models here.
from place.models import City


class Storage(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name
