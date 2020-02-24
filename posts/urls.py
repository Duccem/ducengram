from django.urls import path
from posts import views

urlpatterns = [
    path('',views.PostsFeedView.as_view(),name="feed"),
    path('posts/create/',views.CreatePostView.as_view(),name="create"),
    path('posts/<str:pk>',views.PostDetailView.as_view(),name="detail"),
    path('posts/like/',views.like,name="like"),
    path('posts/dislike/',views.dislike,name="dislike")
]