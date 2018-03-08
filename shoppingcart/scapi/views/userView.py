from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from scapi.models.shoppingcartuser import shoppingcartuser
from scapi.serializers.shoppingcartuserSerializer import shoppingcartuserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = shoppingcartuser.objects.all()
    serializer_class = shoppingcartuserSerializer