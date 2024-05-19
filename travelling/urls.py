from django.urls import path
from .views import TravelListView, TravelDetailView

urlpatterns = [
    path('travel/', TravelListView.as_view(), name='travel'),
    path("travel/<int:id>/", TravelDetailView.as_view(), name="travel-detail"),
]