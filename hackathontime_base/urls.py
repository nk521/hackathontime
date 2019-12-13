"""ht_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from hackathontime_users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('hackathontime_main.urls')),
    path('admin/', admin.site.urls),
    path('register/', users_views.register, name='ht-register'),
    path('login/', auth_views.LoginView.as_view(template_name='hackathontime_users/login.html',
                                                redirect_authenticated_user=True), name='ht-login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='ht-home'), name='ht-logout'),
    path('reset/', auth_views.PasswordResetView.as_view(
        template_name='hackathontime_users/password_reset.html'), name='ht-password-reset'),
    path('reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='ht-password-reset-confirm'),
    path('profile/', users_views.profile, name='ht-profile'),
    path('profile/<slug:profile_slug>',
         users_views.profile_view, name='ht-profile-view'),
    path('team/register', users_views.register_team, name='ht-register-team'),
    path('hackathon/<slug:hackathon_slug>',
         users_views.hackathon_view, name='ht-hackathon-view'),
    path('team/', users_views.team, name='ht-team'),
    path('team/<slug:team_slug>', users_views.team_view, name='ht-team-view'),
    path('team/join/<str:code>', users_views.team_join, name='ht-team-join'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
