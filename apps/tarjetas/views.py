from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from apps.tarjetas.models import Personaje, Tarjeta
from apps.tarjetas.forms import PersonajeForm
from django.urls import reverse_lazy

# Create your views here.


class PersonajeListView(ListView):
    model = Personaje
    ##TODO: template name
class PersonajerDetailView(DetailView):
    model = Personaje
    ##TODO: template name

class PersonajeCreateView(CreateView):
    model = Personaje
    form_class = PersonajeForm
    ##TODO: template name, success_url

class PersonajeUpdateView(UpdateView):
    model = Personaje
    form_class = PersonajeForm
    ##TODO: template name, success_url

class PersonajeDeleteView(DeleteView):
    model = Personaje
    ##TODO: success_url




