from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.view_home,name='home-page'),
    path('posts/',views.view_posts,name='all-posts-page'),
    path('posts/<slug:id>',views.view_post_detail,name='post-details-page')
]
