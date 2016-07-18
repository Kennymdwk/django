from django.contrib import admin
from .models import Code, Product, Supplier, Consumer

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'id_1C', 'supplier', 'consumer')
    # search_fields = ('name', 'weight', 'supplier', 'consumer')
    # filter_horizontal = ('supplier', 'consumer')
    # readonly_fields = ('consumer',)

    # filter_vertical = ('consumer')
    # fields = ('name', 'weight',('supplier','consumer'), 'id_1C')
admin.site.register(Code)
admin.site.register(Supplier)
admin.site.register(Consumer)
admin.site.register(Product, ProductsAdmin)
