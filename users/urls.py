from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('verify/', views.verify_code, name='verify'),
]