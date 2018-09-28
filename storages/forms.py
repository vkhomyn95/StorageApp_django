from django import forms

from storages.models import Storage


class StorageAddForm(forms.ModelForm):

    class Meta:
        model = Storage
        fields = ('name', 'city', 'address')

    def clean_name(self):
        MAX_LENGTH = 25
        user = self.cleaned_data['name']
        if Storage.objects.filter(name=user).exists():
            raise forms.ValidationError('The name %s already exists' % user)
        if len(user) > MAX_LENGTH:
            raise forms.ValidationError('Length of name more than %s' %MAX_LENGTH)
        return user

    def clean_address(self):
        name = self.cleaned_data['address']
        MAX_LENGTH = 25
        if len(name) > MAX_LENGTH:
            raise forms.ValidationError('Length of adresss more than %s' %MAX_LENGTH)
        return name

