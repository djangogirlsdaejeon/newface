# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count

from item.models import Drama, Item, Question


# Create your views here.
@csrf_exempt
def home(request):
    hot_item_list = Item.objects.annotate(reviews_count=Count('review')).order_by('-reviews_count').all()[:5]
    drama = Drama.objects.annotate(items_count=Count('item')).order_by('-items_count').first()
    question_list = Question.objects.values('id', 'title').all()[:5]
    item_list = Item.objects.values('id', 'title').all()[:5]

    return render(request, 'main.html', {'hot_item_list': hot_item_list, 'drama': drama, 'question_list': question_list, 'item_list': item_list}) 

class Items(APIView):

    def get(self, request):
        item_list = Item.objects.filter(status=True).all()

        return Response(dramas)

    def post(self, request):
        json_data = json.loads(request.POST)


        res = {
                'wefwef': 'awefewf'
        }
        return Response(res)

