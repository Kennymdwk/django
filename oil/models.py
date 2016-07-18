from django.db import models
from products.models import Code
# Create your models here.

class Oilio(models.Model):
    income_date = models.DateTimeField('товар получен')
    name = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='наименование продукта')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='от кого')
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, verbose_name='кому')
    id_1C = models.ForeignKey(Code, on_delete=models.CASCADE, verbose_name='идентификатор партии')
    weight = models.FloatField(verbose_name='вес')