from django.shortcuts import reverse, redirect
from django.contrib.auth.decorators import login_required

from ..models import Post
from ..forms import CommentForm


@login_required()
def comment_create(request, post_pk):
    if request.method == "POST":
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment_form.instance.post = Post.objects.get(id=post_pk)
            comment_form.save()
        return redirect(reverse('posts:detail', kwargs={"pk": post_pk}))