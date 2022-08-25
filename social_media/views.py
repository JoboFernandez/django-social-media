from django.shortcuts import redirect, reverse, render
from django.db.models import Q

from users.models import Profile
from posts.models import Post


def home(request):
    return redirect(reverse('posts:global-list'))


def search(request):
    query = request.GET.get("query")
    profiles = Profile.objects.all()
    posts = Post.objects.all()
    if query:
        profiles = profiles.filter(
            Q(user__username__icontains=query)
        )
        posts = posts.filter(
            Q(content__icontains=query)
        )

    context = {
        "profiles": profiles[:5],
        "posts": posts.order_by('-date_posted')[:5],
        "delete_redirect": "/posts",
        "query": query,
    }

    return render(request, "search.html", context=context)