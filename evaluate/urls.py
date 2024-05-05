from django.urls import path
from . import views
from .views import EvaluateListView, EvaluateDetailView, EvaluateCreateView, EvaluateDeleteView

app_name = 'evaluate'

urlpatterns = [
    path('evaluates/', EvaluateListView.as_view(), name='evaluate-list'),
    path('evaluates/<int:cno>/<int:fno>/', EvaluateDetailView.as_view(), name='evaluate-detail'),
    path('evaluates/new/', EvaluateCreateView.as_view(), name='evaluate-new'),
    path('evaluates/delete/<int:cno>/<int:fno>/', EvaluateDeleteView.as_view(), name='evaluate-delete'),
]