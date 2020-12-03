from django.urls import path

from .views import views

urlpatterns = [
    path(r'api/test/', views.index, name='index'),
]
