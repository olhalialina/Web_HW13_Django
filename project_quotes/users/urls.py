from django.urls import path

from . import views

# from django.contrib.auth.views import LogoutView   #LoginView,
from django.contrib.auth.views import LogoutView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

from .forms import LoginForm
from .views import RegisterView  # , LoginView

app_name = "users"

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),

    path('signin/', views.signin, name='signin'),

    # path('signin/', LoginView.as_view(
    #     template_name="users/signin.html",
    #     authentication_form=LoginForm,
    #     redirect_authenticated_user=True
    # ), name='signin'),

    # path('signin/', LoginView.as_view(), name='signin'),
    # path('signup/', views.signup, name='signup'),

    path('logout/', views.logoutuser, name='logoutuser'),

    path('reset-password/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                          success_url='/users/reset-password/complete/'),
         name='password_reset_confirm'),
    path('reset-password/complete/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]