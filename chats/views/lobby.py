from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required

from ..models import Thread


@login_required()
def lobby(request):
    logged_user = request.user
    latest_thread = Thread.objects.by_user(user=logged_user.id).order_by('-updated_at').first()

    if latest_thread:
        other_user = latest_thread.users.exclude(username=logged_user.username).first().username
        return redirect(reverse("chats:personal", kwargs={"username": other_user}))
    else:
        context = {
            'other_user': '...',
            'chat_threads': [],
            'messages': [],
        }
        return render(request, "chats/lobby.html", context=context)

