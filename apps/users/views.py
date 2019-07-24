from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from apps.users.models import User
from apps.users.forms import UserForm
from django.urls import reverse_lazy

class UserListView(ListView):
    model = User
    template_name = 'users.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('users:users')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('users:users')

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users:users')
