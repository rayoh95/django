from django.urls import path
from . import views
from django.conf.urls import url

app_name = "Boards"

urlpatterns = [
    path('', views.boards, name = 'boards'),
    path('create/', views.create_board, name = 'board'),
    path('<int:pk>/update/', views.update_board, name = "update"),
    path('<int:pk>/delete/', views.delete_board, name = "delete"),
    path('<int:pk>/', views.page, name = "page"),
    path('<int:pk>/comment/create/', views.create_comment, name = "comment"),
    path('<int:board_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('<int:board_id>/comments/<int:comment_id>/update/', views.update_comment, name='update_comment'),
]
