from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('notice/', views.notice, name='notice'),
    path('notice/<int:notice_id>/', views.notice_detail, name='notice_detail'),
    path('notice/new/', views.notice_new, name='notice_new'),
    path('notice/<int:notice_id>/delete/', views.notice_delete, name='notice_delete'),
    path('notice/<int:notice_id>/update/', views.notice_update, name='notice_update'),
]