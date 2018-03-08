from django.db import models

class shoppingcartuser(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.first_name +' '+self.last_name

    class Meta:
        app_label = 'scapi'

