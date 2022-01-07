from os import name
from django.contrib import admin
from django.urls import path
from .views import  signup_view, updateprofile , DeleteUser
from django.contrib.auth.views import LoginView , LogoutView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', signup_view.as_view(), name="signup"),
    path('login/' , LoginView.as_view(template_name = 'signup/login.html' , redirect_authenticated_user = 'true') , name = 'login'),
    path('', TemplateView.as_view( template_name = 'signup/home.html'), name='home'),
    path('logout/' , LogoutView.as_view(template_name = 'signup/logout.html') , name = 'logout'),
    path ('update/' ,updateprofile.as_view()  , name = 'update'),
    path('delete/', login_required(DeleteUser.as_view()) , name = 'delete'),
]