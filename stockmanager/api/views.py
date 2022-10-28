from rest_framework import viewsets
from stockmanager.models import Product
from stockmanager.api.serializers import ProductSerializer
from rest_framework.permissions import AllowAny, IsAdminUser


class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
                
  def get_permissions(self):
    if self.request.method == 'GET':
        self.permission_classes = [AllowAny, ]
    else:
        self.permission_classes = [IsAdminUser, ]

    return super(ProductViewSet, self).get_permissions()

               
        

