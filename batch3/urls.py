"""batch3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Attendance import views as att_views
from django.contrib.auth import views as auth_views
from user_app.views import Profile, loginPage, Profile_user
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', att_views.home, name="home" ),
    path('att/', include('Attendance.urls')),
    #path('login/', auth_views.LoginView.as_view(template_name='user_app/login.html'), name='Login'),
    path('login/',loginPage, name='Login'),

    path('profile/',Profile , name='profile'),
    path('profile/<int:id1>',Profile_user , name='profile_user'),

    path('logout/', auth_views.LogoutView.as_view(template_name='user_app/logout.html'), name='Logout'),
    path('user/', include('user_app.urls')),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user_app/password_reset.html'), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='user_app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='user_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user_app/password_reset_complete.html'), name='password_reset_complete'),
    path('blog/', include('blog.urls')),
    
]
urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)