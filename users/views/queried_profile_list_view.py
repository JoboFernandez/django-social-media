from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from ..models import Profile


class QueriedProfileListView(LoginRequiredMixin, ListView):
    template_name = "users/queried_profile_list.html"
    model = Profile
    context_object_name = "profiles"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QueriedProfileListView, self).get_context_data(**kwargs)
        context["query"] = self.request.GET.get('query')
        return context

    def get_queryset(self):
        query = self.request.GET.get('query')
        queryset = Profile.objects.all()
        if query:
            queryset = queryset.filter(
                Q(user__username__icontains=query)
            )
        return queryset

