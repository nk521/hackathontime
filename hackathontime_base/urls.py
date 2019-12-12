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
    path('login/', auth_views.LoginView.as_view(template_name='hackathontime_users/login.html'), name='ht-login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='ht-home'), name='ht-logout'),
    path('profile/', users_views.profile, name='ht-profile'),
    path('profile/<slug:profile_slug>', users_views.profile_view, name='ht-profile-view'),
    path('team/register', users_views.register_team, name='ht-register-team'),
    path('hackathon/<slug:hackathon_slug>', users_views.hackathon_view, name='ht-hackathon-view'),
    path('team/<slug:team_slug>', users_views.team_view, name='ht-team-view'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)