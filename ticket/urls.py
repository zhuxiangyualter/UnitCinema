from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns = [
    path('ticket/', views.buyticket, name='ticket'),
    path('ticket/<int:ticket_id>/', views.cancelticket, name='ticket_detail'),
   ]
