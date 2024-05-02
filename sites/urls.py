from django.urls import path
from . import views

app_name = 'sites'

urlpatterns=[
    path('sites',views.sites,name="sites"),

]
