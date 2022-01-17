from os import name
from django.contrib import admin
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import redirect
from django.urls import path
from .views import  signup_view, updateprofile , DeleteUser
from django.contrib.auth.views import LoginView , LogoutView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('signup/', signup_view.as_view(), name="signup"),
    
    path('login/' , LoginView.as_view(
        template_name = 'signup/login.html' , redirect_authenticated_user = 'true' ) ,
         name = 'login'),
    path('', TemplateView.as_view( 
        template_name = 'signup/home.html'), 
        name='home'),
    path('logout/' , LogoutView.as_view(
        template_name = 'signup/logout.html') , 
        name = 'logout'),
    path ('update/' ,login_required(
        updateprofile.as_view() ) ,
         name = 'update'),
    path('delete/', DeleteUser.as_view() , name = 'delete'),
    
    path(
        'change-password/', auth_views.PasswordChangeView.as_view(
            template_name='signup/change-password.html'
        ),
        name='change_password'
    ),
    #  path('password-reset/',
    #      auth_views.PasswordResetView.as_view(
    #          template_name='signup/password-reset/password_reset.html',
    #          subject_template_name='signup/password-reset/password_reset_subject.txt',
    #          email_template_name='signup/password-reset/password_reset_email.html',
    #          success_url='login'
    #      ),
    #      name='password_reset'),
    # path('password-reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(
    #          template_name='signup/password-reset/password_reset_done.html'
    #      ),
    #      name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(
    #          template_name='signup/password-reset/password_reset_confirm.html'
    #      ),
    #      name='password_reset_confirm'),
    # path('password-reset-complete/',
    #      auth_views.PasswordResetCompleteView.as_view(
    #          template_name='signup/password-reset/password_reset_complete.html'
    #      ),
    #      name='password_reset_compsignu' ) , 
    #               
    ]