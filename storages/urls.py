from django.conf.urls import url

from storages import views

urlpatterns = [
    url(r'^$', views.storage_page, name='storages'),
    url(r'^storage/add/$', views.add_storage, name='add_storage'),
    url(r'^storage/(?P<storage_id>\d+)/$', views.detail_view, name='storages_detail'),
    url(r'^storage/(?P<storage_id>\d+)/delete/$', views.delete_view, name='storage_delete'),
    url(r'^storage/(?P<storage_id>\d+)/update/$', views.update_view, name='storage_update'),
]