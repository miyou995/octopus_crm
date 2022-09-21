from multiprocessing import context
from pipes import Template
from pprint import pprint
from django.shortcuts import render, redirect
import logging
from django.contrib.auth import login, authenticate
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from accounts.models import User
from .froms import UserCreationForm, UserEditForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.utils.functional import lazy
from django.contrib.messages.views import SuccessMessageMixin
from .choice import ROLE_TYPE_CHOICE

# Create your views here.
# logger = logging.getLogger(__name__)

class SignupView(FormView):
    template_name = "signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:signup_success')
    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        email = form.cleaned_data.get("email")
        raw_password = form.cleaned_data.get("password1")
        return response    

class SignupsuccessView(TemplateView):
    template_name = "signup_message.html" 


class UserView(TemplateView):
    model = User
    template_name= "user-detail.html"

    def get_context_data(self, **kwargs):
        context =  super(UserView, self).get_context_data(**kwargs)
        context["roles"] = ROLE_TYPE_CHOICE
        return context
  

class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class= UserEditForm
    template_name = 'profile.html' 
    success_message = "profile updated successfully."
    success_url = reverse_lazy('accounts:profile')

    def get_context_data(self, **kwargs):
        context =  super(UserUpdateView, self).get_context_data(**kwargs)
        context["roles"] = ROLE_TYPE_CHOICE
        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error comited please enter your real informtions")
        return redirect('project:projectlist')
   

class profileView(TemplateView):
    model = User
    template_name= "profile.html"

    def get_context_data(self, **kwargs):
        context =  super(profileView, self).get_context_data(**kwargs)
        context["roles"] = ROLE_TYPE_CHOICE
        return context

# class AddUser()
