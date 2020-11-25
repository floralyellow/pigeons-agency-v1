from django.urls import path

from .views import views

urlpatterns = [
    path(r'test/', views.index, name='index'),
]
