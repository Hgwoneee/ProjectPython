# chargingstations/api/urls.py
from rest_framework.routers import DefaultRouter
from .views import ChargingStationViewSet

router = DefaultRouter()
router.register(r'charging-stations', ChargingStationViewSet)

urlpatterns = router.urls
