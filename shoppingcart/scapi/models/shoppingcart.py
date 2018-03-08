from django.db import models

class shoppingcart(models.Model):
    shoppingCartStatusChoices = ((0,'Pending Checkout'),(1, 'Processing'),(3,'Checked out'));

    shoppingcart_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('shoppingcartuser', on_delete=models.CASCADE, related_name = "shoppingcart")
    created_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_updated_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.CharField(choices = shoppingCartStatusChoices, max_length = 10)

    class Meta:
        app_label = 'scapi'
