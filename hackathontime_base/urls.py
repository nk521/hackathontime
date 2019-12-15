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
    path('register/activate/<uidb64>/<token>/', users_views.activate, name='ht-activate'),
    path('login/', auth_views.LoginView.as_view(template_name='hackathontime_users/login.html',
                                                redirect_authenticated_user=True), name='ht-login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='ht-home'), name='ht-logout'),
    path('reset/', auth_views.PasswordResetView.as_view(
        template_name='hackathontime_users/password_reset.html',
        extra_context={'title': 'Reset Password'}), name='ht-password-reset'),
    path('reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='hackathontime_users/password_reset_confirm.html',
        extra_context={'title': 'Reset Password'}), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='hackathontime_users/password_reset_done.html',
        extra_context={'title': 'Reset Password'}), name='password_reset_done'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='hackathontime_users/password_reset_complete.html',
        extra_context={'title': 'Reset Password'}), name='password_reset_complete'),
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
