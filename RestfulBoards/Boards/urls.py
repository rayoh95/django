from django.urls import path
from . import views

app_name = "Boards"

urlpatterns = [
    path('', views.Boards, name = 'Boards'),
    path('create/', views.Create_post, name = 'Board'),
    path('<int:pk>/update/', views.update_post, name = "update"),
    path('<int:pk>/delete/', views.delete_post, name = "delete"),
    path('page/<int:pk>/', views.page, name = "page"),
    
]