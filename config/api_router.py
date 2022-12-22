from django.conf import settings
from deezerlike.deezer.views import AlbumViewSet, ArtistViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

from deezerlike.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("albums", AlbumViewSet)
router.register("artists", ArtistViewSet)



app_name = "api"
urlpatterns = router.urls
