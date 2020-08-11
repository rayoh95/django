from django.urls import path
from . import views
from django.conf.urls import url

app_name = "posts"

urlpatterns = [
    path('', views.posts, name = 'posts'),
    path('create_post/', views.create_post, name = 'create_post'),
    path('<int:pk>', views.read_post, name = 'read_post'),
]
