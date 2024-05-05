from django.urls import path
from . import views
from .views import LoginAPIView as Login,RegisterAPIView as Register,\
    LogoutAPIView as Logout,UserProfileAPIView as UserProfile,\
    UserProfileEditAPIView as UserProfileEdit,UserRepwdView as UserRepwd
app_name = 'worker'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('user/profile/',UserProfile.as_view(), name='user_profile'),
    path('user/profile/edit', UserProfileEdit.as_view(), name='user_profile_edit'),
    path('user/profile/repwd', UserRepwd.as_view(), name='user_profile_repwd'),
]