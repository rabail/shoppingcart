from django.db import models

class shoppingcartitems(models.Model):
    shoppingcartitem_id = models.AutoField(primary_key=True)
    shoppingcart_id = models.ForeignKey('shoppingcart', on_delete = models.CASCADE, related_name="items")
    item_id = models.IntegerField()

    class Meta:
        unique_together = ('shoppingcart_id','item_id')
        app_label = 'scapi'
