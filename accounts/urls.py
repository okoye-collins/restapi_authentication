from rest_framework import routers
from .views import RegisterUserViewSet, VerifyUserEmailViewSet


router = routers.DefaultRouter()
router.register("register_user", RegisterUserViewSet)
router.register("verify", VerifyUserEmailViewSet, basename="verify")


urlpatterns = router.urls
