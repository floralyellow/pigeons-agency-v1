from rest_framework import routers
from .views.user_view import UserViewSet
from .views.fill_tr_views import FillTRView
from .views.player_views import PlayerLvlupView, PlayerUseBucketView, PlayerView
from .views.pigeons_views import PigeonView, PigeonAttackerView, PigeonDefenderView, PigeonActivateView, PigeonSellView
from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register(r'api/users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path(r'api/pigeons/', PigeonView.as_view(), name='pigeon'),

    path(r'api/pigeons/attacker', PigeonAttackerView.as_view(), name='set_attacker'),
    path(r'api/pigeons/activate', PigeonActivateView.as_view(), name='set_active'),
    path(r'api/pigeons/sell', PigeonSellView.as_view(), name='sell'),
    path(r'api/pigeons/defender', PigeonDefenderView.as_view(), name='set_defender'),


    path(r'api/player/', PlayerView.as_view(), name='player'),
    path(r'api/player/lvlup', PlayerLvlupView.as_view(), name='lvl_up'),
    path(r'api/player/usebucket', PlayerUseBucketView.as_view(), name='usebucket'),




    # ADMIN NO PROD
    path(r'api/tr/', FillTRView.as_view(), name='tr'),

]
# urlpatterns += router.urls
