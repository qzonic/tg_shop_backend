from rest_framework import viewsets

from main.models import (
    Lesson,
    Product,
    Customer,
    Order
)
from .serializers import (
    LessonSerializer,
    ProductSerializer,
    CustomerSerializer,
    OrderSerializer
)


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вьюсет для урока """

    queryset = Lesson.objects.all()
    serializer_class =LessonSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вьюсет для предмета продажи """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """ Вьюсет для покупателя """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """ Вьюсет для заказа """

    serializer_class = OrderSerializer

    def get_customer(self):
        tg_id = self.kwargs.get('tg_id')
        customer = Customer.objects.filter(
            tg_id=tg_id
        ).first()
        return customer

    def get_queryset(self):
        customer = self.get_customer()
        orders = customer.orders.all()
        return orders

    def perform_create(self, serializer):
        serializer.save(customer=self.get_customer())
