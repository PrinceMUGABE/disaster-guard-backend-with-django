# UserApp/urls.py
from django.urls import path
from .views import signup, login, get_user_by_id, get_user_by_email, get_all_users, update_user_by_id, delete_user_by_id, reset_password

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('user/<int:pk>/', get_user_by_id, name='get_user_by_id'),
    path('user/email/<str:email>/', get_user_by_email, name='get_user_by_email'),
    path('users/', get_all_users, name='get_all_users'),
    path('user/update/<int:pk>/', update_user_by_id, name='update_user_by_id'),
    path('user/delete/<int:pk>/', delete_user_by_id, name='delete_user_by_id'),
    path('user/reset-password/<int:pk>/', reset_password, name='reset_password'),
]
