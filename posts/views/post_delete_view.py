from django.shortcuts import reverse
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from ..models import Post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    def get_success_url(self):
        if "user" in self.request.path:
            return reverse("users:profile", kwargs={"pk": self.request.user.id})
        elif "subscribed" in self.request.path:
            return reverse("posts:subscribed-list")
        else:
            return reverse("posts:global-list")

