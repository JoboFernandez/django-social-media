from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from ..models import Follow, Post


@login_required()
def follow(request, post_pk):
    user = request.user
    post = Post.objects.get(id=post_pk)
    try:
        Follow.objects.create(user=user, post=post)
    except IntegrityError:
        pass
    return redirect(request.META.get("HTTP_REFERER"))


@login_required()
def unfollow(request, post_pk):
    user = request.user
    post = Post.objects.get(id=post_pk)
    _follow = Follow.objects.get(user=user, post=post)
    _follow.delete()
    return redirect(request.META.get("HTTP_REFERER"))
