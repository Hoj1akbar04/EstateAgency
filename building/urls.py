from django.urls import path
from .views import HouseListView, HouseDetailView

urlpatterns = [
    path('house/', HouseListView.as_view(), name='built'),
    path("house/<int:id>/", HouseDetailView.as_view(), name="built-detail"),
]