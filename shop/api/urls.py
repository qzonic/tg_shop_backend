from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import (
    LessonViewSet,
    ProductViewSet,
    CustomerViewSet,
    OrderViewSet
)


router = DefaultRouter()

router.register('lessons', LessonViewSet)
router.register('products', ProductViewSet)
router.register('customers', CustomerViewSet)
router.register(r'orders/(?P<tg_id>\d+)',
                OrderViewSet,
                basename='orders'
                )


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
]
