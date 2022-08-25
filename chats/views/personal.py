from django.shortcuts import render
from django.contrib.auth.models import User

from ..models import Message, Thread


def personal(request, username):
    logged_user = request.user
    other_user = User.objects.get(username=username)

    thread = Thread.objects.get_or_create_personal_thread(user1=logged_user, user2=other_user)
    messages = Message.objects.filter(thread=thread).order_by('-created_at')
    _chat_threads = Thread.objects.by_user(user=logged_user.id).order_by('-updated_at')
    chat_threads = [(thread, thread.users.exclude(username=logged_user).first()) for thread in _chat_threads]

    context = {
        'other_user': username,
        'chat_threads': chat_threads,
        'messages': messages,
    }

    return render(request, "chats/personal.html", context=context)

