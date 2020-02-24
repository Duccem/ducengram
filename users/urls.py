from django.urls import path
from django.views.generic import TemplateView
from users import views

urlpatterns = [
    path('<str:username>',views.UserDetailView.as_view(),name='profile'),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    path('signup/',views.SignupView.as_view(),name="signup"),
    path('me/profile/',views.UpdateProfileView.as_view(),name="update"),
    path('follow/',views.follow,name="follow"),
    path('unfollow/',views.unfollow,name="unfollow")
]