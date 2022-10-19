from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.UserLoginViwe.as_view(), name='login'),
    path('logout/', views.UserLogoutViwe.as_view(), name='logout'),
    path('profile/<int:user_id>/', views.ProfileViwe.as_view(), name='profile'),
    path('reset/', views.ResetPaswordView.as_view(), name='reset_pasword'),
    path('reset/done/', views.UserPaswordDoneView.as_view(),
         name='success_url_done'),
    path('confirm/<uidb64>/<token>/', views.UserPaswordConfirmView.as_view(),
         name='success_url_confirm'),
    path('confirm/compelete/', views.UserPaswordCompeleteView.as_view(),
         name='pasword_compelete'),

    path('follow/<int:id_user>/', views.FollowView.as_view(), name='follower'),
    path('unfollow/<int:id_user>/', views.UnFollowView.as_view(), name='unfollow'),

]
