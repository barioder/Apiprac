from rest_framework import routers
from .views import DiscountsViewSet

discount_router = routers.DefaultRouter()
discount_router.register("discounts", DiscountsViewSet, basename="discounts")
discount_router.register("discounts/<int:id>/", DiscountsViewSet, basename="retrieve")