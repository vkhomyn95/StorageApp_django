from django.conf.urls import url

from shops.views import ShopView, ShopDetailView, ShopCreateView, ShopUpdateView, ShopDeleteView

urlpatterns = [
    url(r'^shops/$', ShopView.as_view(), name='shops'),
    url(r'^add_shop/$', ShopCreateView.as_view(), name='create_shop'),
    url(r'^shops-detail/(?P<pk>\d+)/$', ShopDetailView.as_view(), name='shops_detail'),
    url(r'^update-shop/(?P<pk>\d+)/$', ShopUpdateView.as_view(), name='shop_update'),
    url(r'^delete-shop/(?P<pk>\d+)/$', ShopDeleteView.as_view(), name='shops_delete'),

]