# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class ContactFaces(AbstractUser):
    MALE = 0
    FEMALE = 1
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    sex = models.SmallIntegerField(choices=SEX_CHOICES, default=MALE)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.email
