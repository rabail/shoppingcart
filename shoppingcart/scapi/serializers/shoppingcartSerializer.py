from rest_framework import serializers
from scapi.models.shoppingcart import shoppingcart

class shoppingcartSerializer(serializers.ModelSerializer):
    items = serializers.RelatedField(many=True, read_only =True)

    class Meta:
        model = shoppingcart
        fields= ('shoppingcart_id','user_id','created_on','last_updated_on', 'status','items')