from django.db import models
from django.contrib.auth.models import User

from . import Post


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_follower")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_followed")

    def __str__(self):
        return f"{self.user} | {self.post.content[:15]}"

    class Meta:
        unique_together = (('user', 'post'),)

