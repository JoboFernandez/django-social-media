from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from ..models import UserFollow


@login_required()
def follow(request, user_pk):
    follower = request.user
    followed = User.objects.get(id=user_pk)
    try:
        UserFollow.objects.create(follower=follower, followed=followed)
    except IntegrityError:
        pass
    return redirect(request.META.get("HTTP_REFERER"))


@login_required()
def unfollow(request, user_pk):
    follower = request.user
    followed = User.objects.get(id=user_pk)
    _follow = UserFollow.objects.get(follower=follower, followed=followed)
    _follow.delete()
    return redirect(request.META.get("HTTP_REFERER"))