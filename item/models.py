# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    db_table = 'category'

    name = models.CharField(max_length=100)
    link = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class Drama(models.Model):
    db_table = 'drama'

    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DramaEpisode(models.Model):
    db_table = 'drama_episode'

    drama = models.ForeignKey(Drama)
    name = models.CharField(max_length=200)
    brodcasting_date = models.DateField()

    def __str__(self):
        return "{drama} {episode}".format(drama=self.drama.name, episode=self.name)


class Item(models.Model):
    db_table = 'item'

    author = models.ForeignKey(User)
    drama = models.ForeignKey(Drama)
    episode = models.ForeignKey(DramaEpisode, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField()


class ItemPhoto(models.Model):
    db_table = 'item_photo'

    item = models.ForeignKey(Item)
    filename = models.CharField(max_length=30)
    path = models.CharField(max_length=200)


class ItemFeedback(models.Model):
    db_table = 'item_feedback'

    item = models.ForeignKey(Item)
    author = models.ForeignKey(User)
    value = models.BooleanField()


class ItemComment(models.Model):
    db_table = 'item_comment'

    item = models.ForeignKey(Item)
    author = models.ForeignKey(User)
    content = models.TextField()
    

class ItemReview(models.Model):
    db_table = 'item_review'

    item = models.ForeignKey(Item)
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.FloatField()


class Question(models.Model):
    db_table = 'question'

    author = models.ForeignKey(User)
    drama = models.ForeignKey(Drama, null=True)
    episode = models.ForeignKey(DramaEpisode, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()

