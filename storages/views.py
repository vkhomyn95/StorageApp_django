# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from storages.forms import StorageAddForm
from storages.models import Storage


def storage_page(request):
    storages = Storage.objects.all()
    return render(request, 'list_storage.html', {'storages': storages})


def add_storage(request):
    form = StorageAddForm(request.POST or None)
    added = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            added = True
    return render(request, 'add_storage.html', {'form': form, 'added': added})


def detail_view(request, storage_id):
    storage = get_object_or_404(Storage, id=storage_id)
    return render(request, 'storage_detail.html', {'storage': storage})


def delete_view(request, storage_id):
    if request.method == 'POST':
        rem = get_object_or_404(Storage, id=storage_id)
        rem.delete()

    return redirect(reverse('storages'))


def update_view(request, storage_id):
    upd = get_object_or_404(Storage, id=storage_id)
    form = StorageAddForm(request.POST or None, instance=upd)
    if request.method == 'POST':
        if form.is_valid():
            upd.name = form.cleaned_data['name']
            upd.city = form.cleaned_data['city']
            upd.address = form.cleaned_data['address']
            # upd.save(update_fields=('name',))
            upd.save()
    return render(request, 'add_storage.html', {'form': form})
