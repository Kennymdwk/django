from django.contrib import admin
from dal import autocomplete, forms
from .models import Code, Product, Supplier, Consumer, ProductName
#AqXRT0f6PtHd m
#?tbH<QzkD5c_GOKBS034 p
#QjPuVzRpY bu
class ProductsAdmin(admin.ModelAdmin):
    form = autocomplete
    # prepopulated_fields = {'product':('name', '')}
    # class Meta:
    #     model = Product
    list_display = ('name', 'weight', 'id_1C', 'supplier', 'consumer')
    # list_filter = ['name', 'weight']
    # search_fields = ['name', 'weight']
    # # filter_horizontal = ('supplier', 'consumer')
    # readonly_fields = ('consumer',)
    # filter_vertical = ('consumer')
    # fields = ('income_date','name', 'weight','supplier','consumer', 'id_1C')
admin.site.register(ProductName)
admin.site.register(Code)
admin.site.register(Supplier)
admin.site.register(Consumer)
admin.site.register(Product, ProductsAdmin)
#
