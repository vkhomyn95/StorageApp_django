from django import forms

from storages.models import Storage


class StorageAddForm(forms.ModelForm):

    class Meta:
        model = Storage
        fields = ('name', 'city', 'address')

