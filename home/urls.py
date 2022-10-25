from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('post/<int:id_post>/<slug:slug_post>/',
         views.DetailPoatView.as_view(), name='detail'),
    path('post/delete/<int:id_post>/',
         views.DeletePostViwe.as_view(), name='delete'),
    path('post/update/<int:id_post>/',
         views.UpdatePostViwe.as_view(), name='update'),
    path('post/create/',
         views.CreatePostViwe.as_view(), name='create'),
    path('post/<int:id_post>/',
         views.LikeView.as_view(), name='like'),


]
