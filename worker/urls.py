from django.urls import path
from . import views

app_name = 'worker'

urlpatterns = [
  path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('work/', views.user, name='user'),
    path('user/profile/', views.user_profile, name='user_profile'),
    path('user/profile/edit', views.user_profile_edit, name='user_profile_edit'),

]