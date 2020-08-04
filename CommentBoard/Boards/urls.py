from django.urls import path
from . import views
from django.conf.urls import url

app_name = "Boards"

urlpatterns = [
    path('', views.Boards, name = 'Boards'),
    path('create/', views.create_post, name = 'Board'),
    path('<int:pk>/update/', views.update_post, name = "update"),
    path('<int:pk>/delete/', views.delete_post, name = "delete"),
    path('<int:pk>/', views.page, name = "page"),
    path('<int:pk>/comment/create/', views.create_comment, name = "comment"),
    path('<int:board_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('<int:board_id>/comments/<int:comment_id>/update/', views.update_comment, name='update_comment'),
    path('search/', views.search, name='search'),
]
