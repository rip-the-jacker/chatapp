import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from omnibus.api import publish

from chatapp.models import Message


def signup(request):
    if request.method == 'GET':
        return render(request, 'chatapp/signup.html')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'chatapp/login.html')


@login_required
def chat_view(request):
    return render(request, 'chatapp/chat_page.html')


@csrf_exempt
def new_message(request):
    post_data = request.POST
    message = post_data['message']
    user = request.user
    Message.objects.create(user=user, message=post_data['message'])
    publish('chatapp', 'new_msg', {'text': message, 'username': user.username}, sender='server')
    return HttpResponse(json.dumps({'success': True}), content_type="application/json")
