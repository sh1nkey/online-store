from django.contrib import admin

# Register your models here.

from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ['name', 'stripe_product_price_id', 'description', ('price', 'quantity'), 'image', 'category']
    search_fields = ['name']
    ordering = ['-id']


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    model = Basket
    fields = ['product', 'quantity']
