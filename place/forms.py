from django import forms

from place.models import City, Country


class CountryAddForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = ('name',)


class CityAddForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name', 'country')
