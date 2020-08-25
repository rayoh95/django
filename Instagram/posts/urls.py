from django.urls import path
from . import views
from django.conf.urls import url

app_name = "posts"

urlpatterns = [
    path('', views.posts, name = 'posts'),
    path('create/', views.create_post, name = 'create_post'),
    path('<int:pk>/', views.read_post, name = 'read_post'),
    path('<int:pk>/update/', views.update_post, name = 'update_post'),
    path('<int:pk>/delete/', views.delete_post, name = 'delete_post'),
    path('<int:pk>/comments/create/', views.create_comment, name = 'create_comment'),
    path('<int:post_id>/comments/<int:comment_id>/update/', views.update_comment, name = 'update_comment'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.delete_comment, name = 'delete_comment'),
    path('search/', views.search_post, name = 'search_post'),
    path('<int:post_id>/like/', views.like, name = 'like'),
    path('like_list/', views.like_list, name = 'like_list'),
]
