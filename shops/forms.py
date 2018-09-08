from django import forms

from shops.models import Store, TypeOfStore


class TypeOFShopAddForm(forms.ModelForm):

    class Meta:
        model = TypeOfStore
        fields = ('name',)


class ShopAddForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = ('type_of_store', 'name', 'owner', 'sellers', 'storage', 'city', 'address', 'site')
