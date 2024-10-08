from django.db import models
import uuid 

class Product(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=False)
    description = models.TextField(max_length=500)
    image_url= models.URLField()
    shop = models.CharField(max_length=100, null=False)
    sold = models.IntegerField(default=0)