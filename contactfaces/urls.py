from django.conf.urls import url

from contactfaces.views import ContactFacesView, ContactDetailView

urlpatterns = [
    url(r'^contacts/$', ContactFacesView.as_view(), name='contacts'),
    url(r'^contacts-detail/(?P<pk>\d+)/$', ContactDetailView.as_view(), name='contacts_detail'),
]