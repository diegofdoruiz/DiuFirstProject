from django.urls import path
from .views import *
from apps.users.views import UserListView, UserDeleteView, UserDetailView

app_name = 'users'
urlpatterns = [
	path('', UserListView.as_view(), name='users'),
	path('create/', create, name='create'),
	path('<int:pk>', UserDetailView.as_view(), name='detail'),
	path('edit/<int:pk>', edit, name='edit'),
	path('delete/<int:pk>', UserDeleteView.as_view(), name='delete')
]