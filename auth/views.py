# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

import json

# Create your views here.
@csrf_exempt 
def login(request): 
    json_data = json.loads(request.body)
    email = json_data.get('email','')
    password = json_data.get('password','')
    user = User.objects.filter(email=email, password=password).first()

    if user:
        status = 200
        res_obj = {
            "username": user.username,         
            "email": user.email,         
        }
        request.session['auth'] = True
        request.session['user_id'] = user.id
    else:
        status = 403
        res_obj = {}

    res = {
        "status": "good",
        "resource": res_obj
    }

    return JsonResponse(res, status=status)

@csrf_exempt 
def logout(request): 
    del request.session['auth']
    del request.session['user_id']

    res = {
        "status": "good",
        "resource": {}
    }

    return JsonResponse(res, status=200)

@csrf_exempt
def join(request):
    json_data = json.loads(request.body)
    email = json_data.get('email','')
    username = json_data.get('username','')
    password = json_data.get('password','')
    user, created = User.objects.get_or_create(
            username=username,
            email=email,
            password=password)

    if created:
        status = 200
        request.session['auth'] = True
        request.session['user_id'] = user.id
    else:
        status = 403

    res = {
        "status": "good",
        "resource": {}
    }

    return JsonResponse(res, status=status)
