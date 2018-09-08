from django.conf.urls import url

from contactfaces import views
from place.views import CityView, CityDetailView, CityCreateView, CityUpdateView, CityDeleteView

urlpatterns = [
    url(r'^cities/$', CityView.as_view(), name='cities'),
    url(r'^cities-detail/(?P<pk>\d+)/$', CityDetailView.as_view(), name='cities_detail'),
    url(r'^add-city/$', CityCreateView.as_view(), name='add_city'),
    url(r'^update-city/(?P<pk>\d+)/$', CityUpdateView.as_view(), name='update_city'),
    url(r'^delete-city/(?P<pk>\d+)/$', CityDeleteView.as_view(), name='delete_city')
]
