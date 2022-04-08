from django.urls import path
from . import views

app_name = "Boards"

urlpatterns = [
    path('', views.Boards, name = 'Boards'),
    path('create/', views.Create_post, name = 'Board'),
    path('<int:pk>/update/', views.update_post, name = "update"),
    path('<int:pk>/delete/', views.delete_post, name = "delete"),
    path('<int:pk>/', views.page, name = "page"),
    # path('<int:pk>/createreply/',views.createreply, name="createreply"),
]