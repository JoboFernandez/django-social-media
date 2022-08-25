from django.urls import path

from . import views


app_name = "posts"
urlpatterns = [
    path('global/', views.PostListView.as_view(), name='global-list'),
    path('subscribed/', views.SubscribedPostListView.as_view(), name='subscribed-list'),
    path('queried/', views.QueriedPostListView.as_view(), name='queried-list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path('subscribed/<int:pk>/delete/', views.PostDeleteView.as_view(), name='subscribed-delete'),
    path('user/<int:pk>/delete/', views.PostDeleteView.as_view(), name='user-delete'),

    path('<int:post_pk>/comments/create/', views.comment_create, name='comment-create'),
    path('<int:post_pk>/comments/<int:comment_pk>/delete', views.comment_delete, name='comment-delete'),

    path('<int:post_pk>/follow/', views.follow, name='follow'),
    path('<int:post_pk>/unfollow/', views.unfollow, name='unfollow'),
]

