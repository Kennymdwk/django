from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class ProductName(models.Model):
    productName = models.CharField(max_length=250)
    # class Meta:


    def __str__(self):
        return self.productName

class Code(models.Model):
    code = models.CharField(max_length=250)


    def __str__(self):
        return self.code

class Supplier(models.Model):
    s_name = models.CharField(max_length=250)
    def __str__(self):
        return self.s_name

class Consumer(models.Model):
    c_name = models.CharField(max_length=250)
    def __str__(self):
        return self.c_name

class Product(models.Model):
    income_date = models.DateTimeField(verbose_name='товар получен')
    name = models.ForeignKey(ProductName, on_delete=models.CASCADE, verbose_name='наименование продукта')
    # name = models.CharField(max_length=250)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='от кого',
    # default='Цех номер 5'
    )
    consumer = models.ForeignKey(Consumer,
    on_delete=models.CASCADE,
    verbose_name='кому',
    default='ПЦК'
    )
    id_1C = models.ForeignKey(Code, on_delete=models.CASCADE, verbose_name='идентификатор партии')
    weight = models.FloatField(
        verbose_name='вес(в кг)',
        default=0,
        validators=[
            MinValueValidator(0.1)
        ]

    )

    def __str__(self):
        return str(self.name) # + ' - ' + str(self.weight)
    # def __unicode__(self):
    #     return str(self.name) + ' - ' + str(self.weight)


