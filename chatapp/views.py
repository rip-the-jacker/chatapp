import json

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from omnibus.api import publish

from chatapp.models import Message

def signup(request):
    if request.method=='GET':
        return render(request, 'chatapp/signup.html')
    elif request.method=='POST':
        post_data = request.POST
        username = post_data.get('username')
        password = post_data.get('password')
        User.objects.create_user(username=username, password=password)
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse('chat-view'))


def login_user(request):
    if request.method=='GET':
        return render(request, 'chatapp/login.html')
    elif request.method=='POST':
        post_data = request.POST
        username = post_data.get('username')
        password = post_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse('chat-view'))


@login_required
def chat_view(request):
    history = Message.objects.all()
    context = {'history': history}
    return render(request, 'chatapp/chat_page.html', context)


@csrf_exempt
def new_message(request):
    post_data = request.POST
    message = post_data['message']
    user = request.user
    Message.objects.create(user=user, message=post_data['message'])
    #publish('<channel_name>','<message_type>',{<payload>},sender='<sender_id>')
    val = publish('chatapp', 'new_msg', {'text': message, 'username': user.username}, sender='server')
    return HttpResponse(json.dumps({'success':True}), content_type="application/json")
