# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    language = models.CharField(max_length=3, default="ru")
    login = models.CharField(max_length=100, default="None")
    expected_cmd = models.CharField(max_length=100, default="language")
    first_act = models.CharField(max_length=100, default="None")
    second_act = models.CharField(max_length=100, default="None")

    def __str__(self):
        return self.login
