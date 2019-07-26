from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from apps.tarjetas.models import Personaje, Tarjeta
from apps.tarjetas.forms import PersonajeForm
from django.urls import reverse_lazy

# Create your views here.


class PersonajeListView(ListView):
    model = Personaje
    template_name = 'personajes.html'

class PersonajerDetailView(DetailView):
    model = Personaje
    template_name= 'personaje_detail.html'

class PersonajeCreateView(CreateView):
    model = Personaje
    form_class = PersonajeForm
    template_name = 'personaje_form.html'
    success_url= reverse_lazy('personajes:personajes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        personaje = self.request.user
        context['personaje'] = personaje
        return context


class PersonajeUpdateView(UpdateView):
    model = Personaje
    form_class = PersonajeForm
    success_url= 'personajes:personajes'
    template_name = 'personaje_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        personaje = self.request.user
        context['personaje'] = personaje
        return context
    
class PersonajeDeleteView(DeleteView):
    model = Personaje
    success_url = reverse_lazy('personajes:personajes')
   




