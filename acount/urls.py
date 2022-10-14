from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.UserLoginViwe.as_view(), name='login'),
    path('logout/', views.UserLogoutViwe.as_view(), name='logout'),
    path('profile/<int:user_id>/', views.ProfileViwe.as_view(), name='profile'),

]
