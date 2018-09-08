# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from storages.forms import StorageAddForm
from storages.models import Storage


class StorageView(ListView):
    model = Storage
    queryset = Storage.objects.all()
    context_object_name = 'storages'
    template_name = 'list_storage.html'


def add_storage(request):
    form = StorageAddForm((request.POST or None), (request.FILES or None))
    added = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            added = True
    return render(request, 'add_storage.html', {'form': form, 'added': added})


def detail_view(request, storage_id):
    storage = get_object_or_404(Storage, id=storage_id)
    return render(request, 'storage_detail.html', {'storage': storage})