from django.urls import path, include

from api.views import (CountryAPIViewSet, UserAPIViewSet, CityAPIViewSet, AddressAPIViewSet,
                       CommentsAPIViewSet, TestimonialsAPIViewSet, TravelAPIViewSet, BuildAPIViewSet, AgentAPIViewSet, AgencyAPIViewSet)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register('agents', viewset=AgentAPIViewSet)
router.register('agency', viewset=AgencyAPIViewSet)
router.register("country", viewset=CountryAPIViewSet)
router.register("users", viewset=UserAPIViewSet)
router.register("city", viewset=CityAPIViewSet)
router.register("address", viewset=AddressAPIViewSet)
router.register("comments", viewset=CommentsAPIViewSet)
router.register("testimonial", viewset=TestimonialsAPIViewSet)
#router.register("travelling", viewset=TravelAPIViewSet)
router.register("build", viewset=BuildAPIViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('auth/', views.obtain_auth_token),
]