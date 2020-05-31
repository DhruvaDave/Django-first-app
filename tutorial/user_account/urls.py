from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.home,name="user_account"),
    path('login/',LoginView.as_view(template_name='user_account/login.html'),name="login"),
    path('logout/',LogoutView.as_view(template_name='user_account/logout.html'),name="logout"),
    path('register/',views.register,name="register"),
    path('profile/',views.view_profile,name="view_profile"),
    path('profile/edit',views.edit_profile,name="edit_profile"),
    path('msg/<int:user_id>',views.edit_msg,name="edit_msg"),
    path('all/msg',views.all_msg,name="all_msg"),
    path('all_profile/',views.all_profile,name="all_profile"),
    path('all_profile/<int:id>/', views.index_profile, name='index_profile'),
]