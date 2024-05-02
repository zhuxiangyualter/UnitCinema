from django.urls import path
from . import views

app_name = 'evaluate'

urlpatterns = [
    path('evaluate/', views.evaluate, name='evaluate'),
    #增删改差
    path('evaluate/new/', views.evaluate_new, name='evaluate_new'),
    path('evaluate/<int:evaluate_id>/', views.evaluate_detail, name='evaluate_detail'),
    path('evaluate/<int:evaluate_id>/delete/', views.evaluate_delete, name='evaluate_delete'),
    path('evaluate/<int:evaluate_id>/update/', views.evaluate_update, name='evaluate_update'),
  #  path('evaluate/<int:evaluate_id>/comment/', views.evaluate_comment, name='evaluate_comment'), 暂时不要评论
  #  path('evaluate/<int:evaluate_id>/comment/<int:comment_id>/delete/', views.evaluate_comment_delete, name='evaluate_comment_delete'),
  #  path('evaluate/<int:evaluate_id>/comment/<int:comment_id>/update/', views.evaluate_comment_update, name='evaluate_comment_update'),
    path('evaluate/<int:evaluate_id>/like/', views.evaluate_like, name='evaluate_like'),
    path('evaluate/<int:evaluate_id>/dislike/', views.evaluate_dislike, name='evaluate_dislike'),


]