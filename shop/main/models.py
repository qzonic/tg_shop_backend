from django.db import models


class Lesson(models.Model):
    """ Модель урока """

    title = models.CharField(
        max_length=128,
        unique=True
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.title} | {self.slug}'


class Product(models.Model):
    """ Модель предмета продажи """

    title = models.CharField(
        max_length=128,
        unique=True
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='products'
    )
    slug = models.SlugField(unique=True)
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )
    link = models.URLField()

    def __str__(self):
        return f'{self.title} | {self.price}'


class Customer(models.Model):
    """ Модель покупателя """

    tg_id = models.PositiveIntegerField(
        primary_key=True,
        unique=True
    )
    username = models.CharField(
        max_length=128,
        default='Anonymous'
    )

    def __str__(self):
        return str(self.tg_id)


class Order(models.Model):
    """ Модель заказа """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    def __str__(self):
        return f'{self.customer.tg_id} | {self.product.title}'
