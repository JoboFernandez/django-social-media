from django.shortcuts import redirect, reverse

from ..models import Comment


def comment_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(id=comment_pk)
    comment.delete()
    return redirect(reverse("posts:detail", kwargs={"pk": post_pk}))

