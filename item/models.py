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


class Drama(models.Model):
    db_table = 'drama'

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category)


class Item(models.Model):
    db_table = 'item'

    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField()


class ItemPhoto(models.Model):
    db_table = 'item_photo'

    item_id = models.ForeignKey(Item)
    filename = models.CharField(max_length=30)
    path = models.CharField(max_length=200)


class ItemFeedback(models.Model):
    db_table = 'item_feedback'

    item_id = models.ForeignKey(Item)
    author = models.ForeignKey(User)
    value = models.BooleanField()

class ItemComment(models.Model):
    db_table = 'item_comment'

    item_id = models.ForeignKey(Item)
    author = models.ForeignKey(User)
    content = models.TextField()
    

class ItemReview(models.Model):
    db_table = 'item_review'

    item_id = models.ForeignKey(Item)
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.FloatField()

class Question(models.Model):
    db_table = 'question'

    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.TextField()
