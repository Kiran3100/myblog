from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('signup',views.user_signup,name='signup'),
    path('login',views.user_login,name='login'),
    path('profile',views.user_profile,name='profile'),
    path('logout',views.user_logout,name='logout'),
    path('changepwd',views.user_changepwd,name='changepwd'),
    path('post',views.post,name='post'),
    path('userinfo/<int:id>',views.userinfo,name='userinfo'),
    path('update/<int:id>',views.update,name='update'),
]