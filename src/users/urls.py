from django.urls import path

from .views import user_logout, Register, UserLogin

app_name = 'users'

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', Register.as_view(), name='register'),
]
