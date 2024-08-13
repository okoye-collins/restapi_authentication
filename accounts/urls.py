from rest_framework import routers
from .views import RegisterUserViewSet


router = routers.DefaultRouter()
router.register("register_user", RegisterUserViewSet)


urlpatterns = router.urls