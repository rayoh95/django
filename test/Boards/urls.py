from django.urls import path
from . import views 

app_name = "Boards"

urlpatterns = [
    path('', views.list, name="list"),
    path('create/', views.create, name="create"),
    path('update/<int:pk>/', views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    # path('page/<int:pk>/', views.page, name="page"),
]
