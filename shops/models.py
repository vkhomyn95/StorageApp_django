# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.urls import reverse_lazy

from contactfaces.models import ContactFaces
from place.models import City
from storages.models import Storage


class TypeOfStore(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Store(models.Model):
    type_of_store = models.ForeignKey(TypeOfStore)
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(ContactFaces, related_name='owner_in')
    sellers = models.ManyToManyField(ContactFaces, related_name='seller_in')
    storage = models.ForeignKey(Storage)
    city = models.ForeignKey(City)
    address = models.CharField(max_length=50)
    site = models.URLField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('shops_detail', kwargs={'pk': self.pk})
