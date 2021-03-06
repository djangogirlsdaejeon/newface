# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

@csrf_exempt
def login(request): 
    if request.method == 'POST':
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        user = User.objects.filter(email=email).first()

        if user and user.check_password(password) :
            
            request.session['auth'] = True
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('/')
        else:

            message = '정보를 확인해주세요.'
            return render_to_response('message.html', {'message': message}, status=403)
    else:
        return render(request, 'signIn.html')

@csrf_exempt 
def logout(request): 
    del request.session['auth']
    del request.session['user_id']
    del request.session['username']

    return redirect('home')

@csrf_exempt
def join(request):
    if request.method == 'POST':
        email = request.POST.get('email','')
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        import pdb; pdb.set_trace()

        try:
            user = User(email=email, username=username)
            user.set_password(password)
            user.save()
            request.session['auth'] = True
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('home')
        except:
            message = '정보를 확인해주세요!'
            return render_to_response('message.html', {'message': message}, status=403)

    else:
        return render(request, 'signIn.html')
