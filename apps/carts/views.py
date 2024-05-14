from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.carts.models import Cart,CartItem
from apps.carts.serializers import CartSerializer,CartItemSerializer

class CartViewSet(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class CartItemViewSet(ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    