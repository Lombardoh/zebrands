from rest_framework import viewsets
from stockmanager.models import Product
from stockmanager.api.serializers import ProductSerializer, ProductAdminSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from django.db.models import F

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all().order_by('id')
                
  def get_permissions(self):
    if self.request.method == 'GET':
        self.permission_classes = [AllowAny, ]
    else:
        self.permission_classes = [IsAdminUser, ]

    return super().get_permissions()

  def get_serializer_class(self):
    if self.request.user.is_staff:
      return ProductAdminSerializer
    else: 
      return ProductSerializer

  def retrieve(self, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance=instance)
    if not self.request.user.is_staff:
      Product.objects.filter(id = self.kwargs['pk']).update(anonymous_query = F('anonymous_query')+1)
    return Response(serializer.data)
    
               
        

