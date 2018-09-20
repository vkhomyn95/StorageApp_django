# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.urls import reverse_lazy


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country)

    class Meta:
        ordering = ['country', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('cities_detail', kwargs={'pk': self.pk})