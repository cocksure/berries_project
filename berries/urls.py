from django.urls import path

from berries.views import BerriesHomeView, SingleProductView, BasketView, ShopView, OrderCheckView

app_name = 'berries'

urlpatterns = [
    path('', BerriesHomeView.as_view(), name='home-page'),
    path('single-product/', SingleProductView.as_view(), name='single-page'),
    path('basket/', BasketView.as_view(), name='basket-page'),
    path('shop/', ShopView.as_view(), name='shop-page'),
    path('order-check//', OrderCheckView.as_view(), name='order-check'),

]