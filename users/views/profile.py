from django.shortcuts import render
from django.core.paginator import Paginator

from ..models import Profile


def profile(request, pk):
    page = int(request.GET["page"]) if "page" in request.GET else 1
    model_object = Profile.objects.get(user=pk)
    paginator = Paginator(model_object.user.post_set.all().order_by('-date_posted'), 4)
    is_paginated = paginator.num_pages > 1
    page_obj = paginator.page(page)
    object_list = page_obj.object_list
    delete_redirect = "/posts/user"

    context = {
        "object": model_object,
        "is_paginated": is_paginated,
        "page_obj": page_obj,
        "object_list": object_list,
        "delete_redirect": delete_redirect,
    }

    return render(request, "users/profile_detail.html", context)