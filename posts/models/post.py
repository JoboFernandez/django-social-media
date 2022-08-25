from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content[:15]}... by {self.author.username}"

    @property
    def comment_count(self):
        return self.comment_set.all().count()

    @property
    def follow_count(self):
        return self.post_followed.all().count()

    @property
    def followers(self):
        return self.post_followed.values_list('user', flat=True)

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})

