from django.urls import path
from IDCO import views

app_name = "IDCO"

urlpatterns = [
    path('', views.list, name="list"),
    path('create/', views.create, name="create"),
    path('update/<int:pk>/', views.update, name="update"),
]