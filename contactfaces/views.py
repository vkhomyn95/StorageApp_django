# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from contactfaces.models import ContactFaces


class ContactFacesView(ListView):

    model = ContactFaces
    context_object_name = 'contacts'
    template_name = 'contact_faces.html'


class ContactDetailView(DetailView):

    model = ContactFaces
    context_object_name = 'contact'
    template_name = 'contact_detail.html'


def main(request):

    return render(request, 'main.html', {})



