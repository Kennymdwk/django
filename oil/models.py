from django.db import models
from products.models import Product
# Create your models here.

class Oilio(models.Model):
    name_oil = models.CharField(max_length=250)
    in_date = models.DateTimeField('товар получен')

    added_time = models.TimeField(auto_now=True)
    comments = models.TextField()
    # id_1C_oil = models.ForeignKey(Product.id_1C)
    # weight = models.ForeignKey(Product.weight, on_delete=models.CASCADE, verbose_name='вес')
class Proil(models.Model):
    name = models.ForeignKey('products.Product', on_delete=models.CASCADE,)
    code = models.ForeignKey('products.Code', on_delete=models.CASCADE,)