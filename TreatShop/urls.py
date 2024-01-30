from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("products.urls")),
    path("user/", include("userauths.urls")),
    path("password-reset", auth_view.PasswordResetView.as_view(template_name="userauths/password_reset.html"), name="password_reset"),
    path("password-reset/done", auth_view.PasswordResetDoneView.as_view(template_name="userauths/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_view.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password-reset-complete", auth_view.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
