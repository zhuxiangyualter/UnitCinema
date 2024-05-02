from django.urls import path
from . import views

app_name = 'hall'

urlpatterns = [
   path('hall/', views.hall, name='hall'),
   path('hall/<int:hall_id>/', views.hall_detail, name='hall_detail'),

]