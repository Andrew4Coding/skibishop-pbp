from django.db import models
import uuid 

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)