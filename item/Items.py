from rest_framework.views import APIView
from item.models import Item
from rest_framework.response import Response

from item.models import Drama, Item

import json

class Items(APIView):

    def get(self, request):
        drama_list = Drama.objects.all()

        dramas = [drama.name for drama in drama_list]
        return Response(dramas)

    def post(self, request):

        json_data = json.loads(request.body)

        res = {
                'wefwef': 'awefewf'
        }
        return Response(res)
