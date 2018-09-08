# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from shops.forms import ShopAddForm
from shops.models import Store


class ShopView(ListView):

    model = Store
    context_object_name = 'shops'
    template_name = 'list_shop.html'


class ShopDetailView(DetailView):

    model = Store
    context_object_name = 'shops_detail'
    template_name = 'shop_detail.html'


class ShopCreateView(CreateView):

    form_class = ShopAddForm
    model = Store
    template_name = 'add_shop.html'


class ShopUpdateView(UpdateView):

    model = Store
    fields = '__all__'
    template_name = 'add_shop.html'


class ShopDeleteView(DeleteView):

    model = Store
    success_url = reverse_lazy('shops')
    template_name = 'shop_confirm_delete.html'

