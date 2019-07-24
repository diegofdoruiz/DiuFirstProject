from django.urls import path
from .views import *
from apps.users.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, UserDetailView

app_name = 'users'
urlpatterns = [
	path('', UserListView.as_view(), name='users'),
	path('create/', UserCreateView.as_view(), name='create'),
	path('<int:pk>', UserDetailView.as_view(), name='detail'),
	path('edit/<int:pk>', UserUpdateView.as_view(), name='edit'),
	path('delete/<int:pk>', UserDeleteView.as_view(), name='delete')
]