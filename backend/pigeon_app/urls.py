from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views.adventure_views import AdventureView
from .views.all_players_views import AllPlayersForAttackView, AllPlayersView
from .views.attack_views import AttackView
from .views.pigeons_views import (
    ExpeditionView,
    PigeonActivateView,
    PigeonSellView,
    PigeonTeamAView,
    PigeonTeamBView,
    PigeonView,
)
from .views.player_views import (
    PlayerChangeDefenseTeamView,
    PlayerLvlupView,
    PlayerUseBucketView,
    PlayerView,
)
from .views.user_views import UserViewSet

router = routers.SimpleRouter()
router.register(r"api/users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(r"api/expeditions/", ExpeditionView.as_view(), name="expeditions"),
    path(r"api/pigeons/", PigeonView.as_view(), name="pigeon"),
    path(r"api/pigeons/activate", PigeonActivateView.as_view(), name="set_active"),
    path(r"api/pigeons/sell", PigeonSellView.as_view(), name="sell"),
    path(r"api/pigeons/teama", PigeonTeamAView.as_view(), name="set_in_team_A"),
    path(r"api/pigeons/teamb", PigeonTeamBView.as_view(), name="set_in_team_B"),
    path(r"api/attack", AttackView.as_view(), name="attack"),
    path(r"api/player/", PlayerView.as_view(), name="player"),
    path(r"api/player/lvlup", PlayerLvlupView.as_view(), name="lvl_up"),
    path(
        r"api/player/changedefenseteam",
        PlayerChangeDefenseTeamView.as_view(),
        name="change_defense_team",
    ),
    path(r"api/player/usebucket", PlayerUseBucketView.as_view(), name="usebucket"),
    path(r"api/leaderboard", AllPlayersView.as_view(), name="leaderboard"),
    path(r"api/attacklist", AllPlayersForAttackView.as_view(), name="attacklist"),
    path(r"api/adventure", AdventureView.as_view(), name="adventure"),
]
# urlpatterns += router.urls
