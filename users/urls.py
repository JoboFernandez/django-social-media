from django.urls import path

from . import views


app_name = "users"
urlpatterns = [
    path("queried/", views.QueriedProfileListView.as_view(), name="queried-list"),
    path("<int:pk>/", views.profile, name="profile"),
    path("<int:pk>/update/", views.ProfileUpdateView.as_view(), name="update"),

    path("<int:user_pk>/follow/", views.follow, name="follow"),
    path("<int:user_pk>/unfollow/", views.unfollow, name="unfollow"),
]

