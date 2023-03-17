from django.contrib import admin

from .models import (
    Lesson,
    Product,
    Customer,
    Order
)


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug'
    )
    list_display_links = (
        'title',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'lesson',
        'slug',
        'price'
    )


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'tg_id',
        'username'
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'customer'
    )


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
