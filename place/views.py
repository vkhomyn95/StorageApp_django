# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from place.forms import CountryAddForm, CityAddForm
from place.models import City


class CityView(ListView):

    model = City
    context_object_name = 'cities'
    template_name = 'list_cities.html'


class CityDetailView(DetailView):
    model = City
    context_object_name = 'cities_detail'
    template_name = 'city_detail.html'


class CityCreateView(CreateView):

    form_class = CityAddForm
    model = City
    template_name = 'add_city.html'


class CityUpdateView(UpdateView):

    model = City
    fields = '__all__'
    template_name = 'add_city.html'


class CityDeleteView(DeleteView):

    model = City
    success_url = reverse_lazy('cities')
    template_name = 'city_confirm_delete.html'
