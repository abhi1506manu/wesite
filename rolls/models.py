# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name