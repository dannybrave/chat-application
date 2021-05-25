from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Message,DirectMessage,AllChat


all_users = User.objects.all()
all_messages = Message.objects.all()
direct_messages = DirectMessage.objects.all()


def index(request):

    all_chats = AllChat.objects.filter(user=request.user).order_by('timestamp')
    context={
        'all_chats':all_chats,
        'all_users':all_users
    }
    return render(request,'index.html',context)