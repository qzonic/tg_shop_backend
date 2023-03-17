from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from main.models import (
    Lesson,
    Product,
    Customer,
    Order
)
from rest_framework.response import Response

from .serializers import (
    LessonSerializer,
    ProductSerializer,
    CustomerSerializer,
    OrderSerializer
)


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вьюсет для урока """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = 'slug'


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вьюсет для предмета продажи """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        lesson_slug = self.kwargs.get('lesson_slug')
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        return super().get_queryset().filter(lesson=lesson)


class CustomerViewSet(viewsets.ModelViewSet):
    """ Вьюсет для покупателя """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'post']


class ListCreateModelMixin(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    pass


class OrderViewSet(ListCreateModelMixin):
    """ Вьюсет для заказа """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    product_serializer = ProductSerializer
    http_method_names = ['get', 'post']

    def get_customer(self):
        tg_id = self.kwargs.get('tg_id')
        customer = get_object_or_404(Customer, tg_id=tg_id)
        return customer

    def get_queryset(self):
        customer = self.get_customer()
        queryset = customer.orders.all()
        # if self.request.method == 'GET':
        #     queryset = [item.product for item in queryset]
        return queryset

    def get_serializer_class(self):
        # if self.request.method == 'GET':
        #     return self.product_serializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(customer=self.get_customer())
