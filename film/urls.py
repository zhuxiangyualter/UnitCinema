from django.urls import path
from . import views

app_name = 'film'

urlpatterns = [
    #用户端
    path('film/', views.film, name='film'),
    path('film/<int:film_id>/', views.film_detail, name='film_detail'),
    #管理端
    #  增删改差电影
    path('film/new/', views.film_new, name='film_new'),
    path('film/<int:film_id>/delete/', views.film_delete, name='film_delete'),
    path('film/<int:film_id>/update/', views.film_update, name='film_update'),
]