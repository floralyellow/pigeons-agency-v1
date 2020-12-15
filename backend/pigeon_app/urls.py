from rest_framework import routers
from .views.views import UserViewSet
from .views.fill_tr_views import FillTRView
from .views.pigeon_view import PigeonView
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
    
    #path(r'api/test/', TestView.as_view(), name='test'),
    path(r'api/pigeons/', PigeonView.as_view(), name='pigeon'),


    # ADMIN NO PROD
    path(r'api/tr/', FillTRView.as_view(), name='tr'),


    #path(r'api/get_test_players/', get_test_players, name='get_test_players'),
]
# urlpatterns += router.urls
