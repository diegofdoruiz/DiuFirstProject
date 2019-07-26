from django.urls import path
from apps.tarjetas.views import PersonajeCreateView, PersonajeUpdateVIew, PersonajeListView, PersonajeDeleteView, PersonajeDetailView

 app_name = 'personajes'
 urlpatterns = [
	path('', PersonajeListView.as_view(), name='personajes'),
	path('create/', PersonajeCreteView.as_view(), name='create'),
	path('<int:pk>', PersonajeDetailView.as_view(), name='detail'),
	path('edit/<int:pk>', PersojeUpdateView().as_view(), name='edit'),
	path('delete/<int:pk>',PersonajeDeleteView.as_view(), name='delete'),
]