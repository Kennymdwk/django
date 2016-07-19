from django.db import models

class Code(models.Model):
    code = models.CharField(max_length=250, verbose_name='Код 1С')

    def __str__(self):
        return self.code

class Supplier(models.Model):
    s_name = models.CharField(max_length=250, verbose_name='Название организации')

    def __str__(self):
        return self.s_name

class Consumer(models.Model):
    c_name = models.CharField(max_length=250, verbose_name='Название склада')

    def __str__(self):
        return self.c_name

class Product(models.Model):
    income_date = models.DateTimeField('товар получен')
    name = models.CharField(max_length=250, verbose_name='наименование продукта')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='от кого')
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, verbose_name='кому')
    id_1C = models.ForeignKey(Code, on_delete=models.CASCADE, verbose_name='идентификатор партии')
    weight = models.FloatField(verbose_name='вес')

    def __str__(self):
        return self.name + ' - ' + str(self.weight)


