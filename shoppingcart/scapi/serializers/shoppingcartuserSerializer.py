from rest_framework import serializers
from scapi.models.shoppingcartuser import shoppingcartuser

class shoppingcartuserSerializer(serializers.ModelSerializer):
    shoppingcart = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = shoppingcartuser
        fields = ('user_id','first_name','last_name','shoppingcart')