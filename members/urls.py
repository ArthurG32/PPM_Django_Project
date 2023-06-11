from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePasswordView, ShowProfileView, EditProfileInfoView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', ChangePasswordView.as_view(), name='change_password'),
    path('profile/<int:pk>/', ShowProfileView.as_view(), name='show_profile'),
    path('edit_profile_info/<int:pk>/', EditProfileInfoView.as_view(), name='edit_profile_info'),

]
