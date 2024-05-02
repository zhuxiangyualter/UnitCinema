from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('worker/profile/', views.worker_profile, name='worker_profile'),
    path('worker/profile/edit', views.worker_profile_edit, name='worker_profile_edit'),

]