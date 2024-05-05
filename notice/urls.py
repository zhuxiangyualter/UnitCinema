from django.urls import path
from . import views
from .views import NoticeListView, NoticeDetailView, NoticeCreateView, NoticeDeleteView
app_name = 'notice'

urlpatterns = [
    path('notices/', NoticeListView.as_view(), name='notice-list'),
    path('notices/<int:notice_id>/', NoticeDetailView.as_view(), name='notice-detail'),
    path('notices/new/', NoticeCreateView.as_view(), name='notice-new'),
    path('notices/delete/<int:notice_id>/', NoticeDeleteView.as_view(), name='notice-delete'),
]