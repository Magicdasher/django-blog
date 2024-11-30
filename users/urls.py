from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # Logowanie
    path('logout/', views.custom_logout, name='logout'),  # Wylogowanie
    path('blog/', views.blog_home, name='blog_home'),

]
