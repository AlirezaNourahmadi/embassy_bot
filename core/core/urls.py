from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from bot.views import ReservationRequestViewSet
from users.views import UserProfileViewSet

router = DefaultRouter()
router.register(r"users", UserProfileViewSet, basename="user")
router.register(r"reservations", ReservationRequestViewSet, basename="reservation")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
