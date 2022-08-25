from django.db import models
from django.contrib.auth.models import User


class UserFollow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")

    def __str__(self):
        return f"{self.follower.username} -> {self.followed.username}"

    class Meta:
        unique_together = (('follower', 'followed'),)

