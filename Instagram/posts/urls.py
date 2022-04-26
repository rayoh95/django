from django.urls import path
from . import views
from django.conf.urls import url

app_name = "posts"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('posts/', views.posts, name = 'posts'),
    path('<int:user_id>/posts/create/', views.create_post, name = 'create_post'),
    path('<int:user_id>/posts/<int:pk>/', views.read_post, name = 'read_post'),
    path('<int:user_id>/posts/<int:pk>/update/', views.update_post, name = 'update_post'),
    path('<int:user_id>/posts/<int:pk>/delete/', views.delete_post, name = 'delete_post'),
    path('<int:user_id>/posts/<int:pk>/comments/', views.read_comments, name = 'read_comments'),
    path('<int:user_id>/posts/<int:pk>/comments/create/', views.create_comment, name = 'create_comment'),
    path('<int:user_id>/posts/<int:post_id>/comments/<int:comment_id>/update/', views.update_comment, name = 'update_comment'),
    path('<int:user_id>/posts/<int:post_id>/comments/<int:comment_id>/delete/', views.delete_comment, name = 'delete_comment'),
    path('posts/search/', views.search_post, name = 'search_post'),
    path('<int:user_id>/posts/<int:post_id>/like/', views.like, name = 'like'),
    # path('posts/like_list/', views.like_list, name = 'like_list'),
    path('posts/my_page/', views.my_page, name = 'my_page'),
]
