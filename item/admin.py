# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(Drama)
admin.site.register(DramaEpisode)
admin.site.register(Item)
admin.site.register(ItemPhoto)
admin.site.register(ItemFeedback)
admin.site.register(ItemComment)
admin.site.register(ItemReview)
admin.site.register(Question)
