from rest_framework.routers import DefaultRouter
from myapp.views import Growth

router = DefaultRouter()
router.register("office",Growth)