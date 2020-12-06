from django.urls import path

from .views import views

urlpatterns = [
    path(r'api/create_test_player/', views.create_test_player, name='create_test_player'),
    path(r'api/get_test_players/', views.get_test_players, name='get_test_players'),
]
