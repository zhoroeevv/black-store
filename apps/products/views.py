from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from apps.products.permissions import ProductPermission

class ProductAPI(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('title', 'description', 'price')
    search_fields = ('title', 'description', 'price')

    def get_permissions(self):
        if self.action == 'retrieve':
            return (IsAuthenticated(), )
        if self.action in ('update', 'partial_update', 'destroy'):
            return (ProductPermission(), )
        return (AllowAny(), )
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)