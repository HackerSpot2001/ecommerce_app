from rest_framework.serializers import ModelSerializer
from .models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['product_id',"category","currency","product_price","product_title","product_description"]