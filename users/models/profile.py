from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.user.username} Profile"

    @property
    def post_count(self):
        return self.user.post_set.all().count()

    @property
    def follower_count(self):
        return self.user.followed.all().count()

    @property
    def followers(self):
        return self.user.followed.values_list('follower', flat=True)

