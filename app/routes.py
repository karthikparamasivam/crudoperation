from rest_framework.routers import DefaultRouter
from app.views import Journey

router = DefaultRouter()
router.register("student",Journey)