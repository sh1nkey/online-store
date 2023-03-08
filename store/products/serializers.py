from rest_framework import serializers

from products.models import ProductCategory
from products.views import Product

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name',queryset=ProductCategory.objects.all())
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image', 'category')
