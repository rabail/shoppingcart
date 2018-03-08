from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from scapi.models.shoppingcart import shoppingcart
from scapi.serializers.shoppingcartSerializer import shoppingcartSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = shoppingcart.objects.all()
    serializer_class = shoppingcartSerializer