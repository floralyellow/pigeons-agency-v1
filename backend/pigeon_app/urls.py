from rest_framework import routers
from .views.user_views import UserViewSet
from .views.player_views import PlayerLvlupView, PlayerUseBucketView, PlayerView
from .views.pigeons_views import PigeonView, PigeonTeamView, PigeonActivateView, PigeonSellView, PigeonDefenderOrderView, ExpeditionView
from .views.attack_views import AttackView
from .views.all_players_views import AllPlayersView, AllPlayersForAttackView
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

    path(r'api/expeditions/', ExpeditionView.as_view(), name='expeditions'),
    path(r'api/pigeons/', PigeonView.as_view(), name='pigeon'),

    path(r'api/pigeons/activate', PigeonActivateView.as_view(), name='set_active'),
    path(r'api/pigeons/sell', PigeonSellView.as_view(), name='sell'),
    path(r'api/pigeons/team', PigeonTeamView.as_view(), name='set_in_team'),
    
    path(r'api/attack', AttackView.as_view(), name='attack'),


    # TODO validate json/array data
    path(r'api/pigeons/organisedefenders', PigeonDefenderOrderView.as_view(), name='organise_defenders'),

    path(r'api/player/', PlayerView.as_view(), name='player'),
    path(r'api/player/lvlup', PlayerLvlupView.as_view(), name='lvl_up'),
    path(r'api/player/usebucket', PlayerUseBucketView.as_view(), name='usebucket'),

    path(r'api/leaderboard', AllPlayersView.as_view(), name='leaderboard'),
    path(r'api/attacklist', AllPlayersForAttackView.as_view(), name='attacklist'),



]
# urlpatterns += router.urls
