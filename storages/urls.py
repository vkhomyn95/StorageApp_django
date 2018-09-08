from django.conf.urls import url

from storages import views
from storages.views import StorageView

urlpatterns = [
    url(r'^storages', StorageView.as_view(), name='storages'),
    url(r'^add-storage', views.add_storage, name='add_storage'),
    url(r'^storages-detail', views.detail_view, name='storages_detail'),
]