from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.views.generic.edit import FormView, UpdateView , DeleteView
from core.accounts.forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from core.accounts import forms


class DeleteUser(DeleteView):
    # specify the model you want to use
    model = User
    template_name = 'signup/delete.html'
    success_url ="accounts/login"
    def get_object(self, queryset=None):
        return self.request.user

class updateprofile(UpdateView):
    model = User
    template_name = 'signup/update.html'
    fields = ['username' , 'email' ]
    def get_object( self, queryset=None):
        return self.request.user
    success_url =  '/accounts/home'


class signup_view(FormView):
    template_name = 'signup/signup.html'
    form_class = SignUpForm
  
    def get(self , request):
        return render(request , self.template_name , {'form' : self.form_class} )
    
    def post(self , request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.save() 
            self.request.session[self.request.user.id] = True
            return redirect('login')
        return render(request , self.template_name , {'form' : form})


