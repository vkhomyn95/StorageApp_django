from django import forms

from storages.models import Storage


class StorageAddForm(forms.ModelForm):

    class Meta:
        model = Storage
        fields = ('name', 'city', 'address')

    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            match = Storage.objects.get(name=name)
        except:
            return self.cleaned_data['name']
        raise forms.ValidationError('Username already exist')

        # if Storage.objects.filter(name=user).exists():
        #     raise forms.ValidationError('The name %s already exists' % user)
        # return user

    def val_address(self):
        name = self.cleaned_data['name']
        MAX_LENGTH = 5
        if len(name) > MAX_LENGTH:
            raise forms.ValidationError('Password %s should not have more %s ' % MAX_LENGTH)
    # def clean_content(self):
    #     min_len = 5
    #     content = self.cleaned_data.get('address')
    #     if len(content) > min_len:
    #         raise forms.ValidationError('content should {0}k'.format(min_len))
    #     return content
