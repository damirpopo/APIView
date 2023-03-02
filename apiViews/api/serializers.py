from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    size = serializers.CharField(max_length=100)
    price= serializers.IntegerField()
    class Meta:
        model = Product
        fields = '__all__'


def update(self,instance,validated_data):
    instance.name = validated_data.get("name", instance.name)
    instance.size = validated_data.get("size", instance.size)
    instance.price= validated_data.get("price", instance.price)
    instance.save()
    return instance