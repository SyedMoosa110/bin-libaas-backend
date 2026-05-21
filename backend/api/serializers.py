from rest_framework import serializers
from .models import Product, Order, Message, StoreSettings, ProductImage, HeroBanner

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image']

    def get_image(self, obj):
        if not obj.image:
            return None
        image_str = str(obj.image)
        if image_str.startswith('http://') or image_str.startswith('https://'):
            return image_str
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url

class ProductSerializer(serializers.ModelSerializer):
    gallery = ProductImageSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, obj):
        if not obj.image:
            return None
        image_str = str(obj.image)
        if image_str.startswith('http://') or image_str.startswith('https://'):
            return image_str
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class StoreSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreSettings
        fields = '__all__'

class HeroBannerSerializer(serializers.ModelSerializer):
    bg_image = serializers.ImageField(use_url=True)
    left_image = serializers.ImageField(use_url=True)
    right_image = serializers.ImageField(use_url=True)

    class Meta:
        model = HeroBanner
        fields = ['id', 'title', 'subtitle', 'bg_image', 'left_image', 'right_image', 'is_active']
