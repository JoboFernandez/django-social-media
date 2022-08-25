from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.db.models import Q

from ..models import Post, Follow, Comment


class PostListView(LoginRequiredMixin, ListView):
    template_name = 'posts/global_post_list.html'
    model = Post
    ordering = ['-date_posted']
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["delete_redirect"] = "/posts"
        return context


class SubscribedPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/subscribed_post_list.html"
    model = Post
    ordering = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        user = self.request.user
        followed_users = user.follower.values('followed')
        followed_posts = Follow.objects.filter(user=user).values('post')
        commented_posts = Comment.objects.filter(author=user).values('post')

        queryset1 = Post.objects.filter(id__in=followed_posts)
        queryset2 = Post.objects.filter(author__in=followed_users)
        queryset3 = Post.objects.filter(id__in=commented_posts)
        queryset = queryset1 | queryset2 | queryset3
        return sorted(queryset, key=lambda instance: instance.date_posted, reverse=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SubscribedPostListView, self).get_context_data(**kwargs)
        context["delete_redirect"] = "/posts/subscribed"
        return context


class QueriedPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/queried_post_list.html"
    model = Post
    ordering = ['-date_posted']

    def get_queryset(self):
        query = self.request.GET.get('query')
        queryset = Post.objects.all()
        if query:
            queryset = queryset.filter(
                Q(content__icontains=query)
            )
        return queryset.order_by('-date_posted')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QueriedPostListView, self).get_context_data(**kwargs)
        context["delete_redirect"] = "/posts"
        context["query"] = self.request.GET.get('query')
        return context

