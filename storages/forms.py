from django import forms

from storages.models import Storage


class StorageAddForm(forms.ModelForm):

    class Meta:
        model = Storage
        fields = ('name', 'city', 'address')

    def clean_name(self):
        user = self.cleaned_data['name']
        if Storage.objects.filter(name=user).exists():
            raise forms.ValidationError('The name %s already exists' % user)
        return user

    def clean_address(self):
        name = self.cleaned_data['address']
        MAX_LENGTH = 5
        if len(name) > MAX_LENGTH:
            raise forms.ValidationError('Name cointainc %d more 5 letters' %MAX_LENGTH)
        return name
