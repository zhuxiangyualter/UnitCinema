from django.urls import path
from . import views
from .views import FilmListAPIView, FilmDetailAPIView, FilmCreateAPIView, FilmDeleteAPIView, FilmUpdateAPIView
app_name = 'film'

urlpatterns = [
    path('film/', FilmListAPIView, name='film'),
    path('film/<int:film_id>/', FilmDetailAPIView, name='film_detail'),
    path('film/new/', FilmCreateAPIView, name='film_new'),
    path('film/delete/<int:film_id>/', FilmDeleteAPIView, name='film_delete'),
    path('film/update/<int:film_id>/', FilmUpdateAPIView, name='film_update'),

]