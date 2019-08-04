from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from accounts import views as account_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),

    path('accounts/', include('accounts.urls')),
    path('apply/', include('appliedunis.urls')),
    path('contact/', include('contact.urls')),
    path('send-feedback/', include('feedback.urls')),
    path('interested/', include('interestedunis.urls')),
    path('administration/', include('staff.urls', namespace='staff')),
    path('universities/', include('universities.urls')),

    path('recover-password/', account_view.PasswordReset.as_view(), name='password_reset'),
    path('recover-password/done/', account_view.PasswordResetDone.as_view(), name='password_reset_done'),
    re_path('^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', account_view.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', account_view.PasswordResetComplete.as_view(), name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)