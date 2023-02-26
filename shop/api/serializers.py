from rest_framework import serializers

from main.models import (
    Lesson,
    Product,
    Customer,
    Order
)


class LessonSerializer(serializers.ModelSerializer):
    """ Сериалайзер для урока """

    class Meta:
        model = Lesson
        fields = ('title', 'slug')
        read_only_fields = ('title', 'slug')


class ProductSerializer(serializers.ModelSerializer):
    """ Сериалайзер для предмета продажи """

    lesson = serializers.SlugRelatedField(
        slug_field='slug',
        read_only=True
    )

    class Meta:
        model = Product
        fields = (
            'title',
            'lesson',
            'slug',
            'price',
            'link'
        )


class CustomerSerializer(serializers.ModelSerializer):
    """ Сериалайзер для покупателя """

    class Meta:
        model = Customer
        fields = ('tg_id', 'username')


class OrderSerializer(serializers.ModelSerializer):
    """ Сериалайзер для заказа """

    product = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Product.objects
    )
    customer = serializers.SlugRelatedField(
        slug_field='tg_id',
        queryset=Customer.objects,
        required=False
    )

    class Meta:
        model = Order
        fields = ('product', 'customer')
