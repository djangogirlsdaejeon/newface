# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response

from item.models import Drama, Item


# Create your views here.
@csrf_exempt
def home(request):
    return render(request, 'main.html') 

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

