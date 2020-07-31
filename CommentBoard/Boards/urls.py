from django.urls import path
from . import views
from django.conf.urls import url

app_name = "Boards"

urlpatterns = [
    path('', views.Boards, name = 'Boards'),
    path('create/', views.Create_post, name = 'Board'),
    path('<int:pk>/update/', views.update_post, name = "update"),
    path('<int:pk>/delete/', views.delete_post, name = "delete"),
    path('<int:pk>/', views.page, name = "page"),
    path('<int:pk>/comment/create/', views.Create_comment, name = "comment"),
   path('<int:board_id>/comments/<int:comment_id>/delete/', views.Delete_comment, name='delete_comment'),
]
