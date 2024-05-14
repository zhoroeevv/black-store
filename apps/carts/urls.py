from django.urls import path
from apps.carts.views import CartViewSet, CartDetailAPI, CartItemViewSet, CartItemDetailAPI


urlpatterns = [
    path('carts/', CartViewSet.as_view(), name='api_carts/'),
    path('carts/<int:pk>/', CartDetailAPI.as_view(), name="api_carts_detail"),
    path('cartitem/', CartItemViewSet.as_view(), name='api_cartitem/'),
    path('cartitem/<int:pk>/', CartItemDetailAPI.as_view(), name="api_cartitem_detail"),
]