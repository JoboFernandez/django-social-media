from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView

from ..models import Post
from ..forms import PostForm


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/post_form.html"
    model = Post
    fields = ['content']

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['form'] = PostForm()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)