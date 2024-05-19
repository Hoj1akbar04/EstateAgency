from django.db.models import Count
from django.db.models.functions.text import Length
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import (Users, Country, Agents, Agency, City, Address, Comments, Testimonials)
from building.models import Build
from travelling.models import Travel
from api.serializers import (CountrySerializer, AgentSerializer, AgencySerializer, UserSerializer, AddressSerializer,
                            CitySerializer, CommentsSerializer, TestimonialsSerializer, TravelSerializer, BuildSerializer)
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination


class TravelAPIViewSet(ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter,]
    search_fields = ['name',]
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]


class BuildAPIViewSet(ModelViewSet):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter,]
    search_fields = ['name',]
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

    @action(detail=True, methods=['get'])
    def see(self, request, *args, **kwargs):
        build = self.get_object()
        with atomic():
            build.saw += 1
            build.save()
            return Response(status=status.HTTP_204_NO_CONTENT)


class AgentAPIViewSet(ModelViewSet):
    queryset = Agents.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [filters.SearchFilter,]
    search_fields = ['first_name', 'last_name',]
    authentication_classes = [TokenAuthentication,]
    pagination_class = LimitOffsetPagination


class AgencyAPIViewSet(ModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    permission_classes = [IsAuthenticated,]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter,]
    search_fields = ['name',]
    authentication_classes = [TokenAuthentication,]


class CountryAPIViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def recently_updated_countries(self, request, *args, **kwargs):
        recently_updated_countries = Country.objects.order_by('-last_update')[:3]
        serialized_data = self.get_serializer(recently_updated_countries, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def countries_with_long_names(self, request):
        countries_with_long_names = Country.objects.annotate(name_length=Length('name')).filter(name_length__gt=4)[:3]
        serialized_data = self.get_serializer(countries_with_long_names, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def countries_starting_with_a(self, request, *args, **kwargs):
        countries_starting_with_a = Country.objects.filter(name__istartswith='U')[:3]
        serialized_data = self.get_serializer(countries_starting_with_a, many=True).data
        return Response(serialized_data)



class UserAPIViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    pagination_class = LimitOffsetPagination
    search_fields = ('first_name', 'last_name', 'email', )

    @action(detail=False, methods=['get'])
    def users_with_image(self, request):
        # Rasmga ega foydalanuvchilarni qaytaradi.
        users_with_image = Users.objects.exclude(image__isnull=True)[:3]
        serialized_data = self.get_serializer(users_with_image, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def users_with_phone_number(self, request):
        # Telefon raqami mavjud foydalanuvchilarni qaytaradi.
        users_with_phone_number = Users.objects.exclude(phone_number__isnull=True)[:3]
        serialized_data = self.get_serializer(users_with_phone_number, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def users_with_address(self, request):
        # Manzili mavjud foydalanuvchilarni qaytaradi.
        users_with_address = Users.objects.exclude(address__isnull=True)[:3]
        serialized_data = self.get_serializer(users_with_address, many=True).data
        return Response(serialized_data)


class CityAPIViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def recently_updated_cities(self, request):
        recently_updated_cities = City.objects.order_by('-last_update')[:3]
        serialized_data = self.get_serializer(recently_updated_cities, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def cities_in_specific_country(self, request):
        country_name = "UZB"
        cities_specific_country = City.objects.filter(country__name=country_name)[:3]
        serialized_data = self.get_serializer(cities_specific_country, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def cities_starting_with_letter(self, request):
        # "T" harfiga boshlangan shaharlar
        letter = "T"
        cities_start_letter = City.objects.filter(name__istartswith=letter)[:3]
        serialized_data = self.get_serializer(cities_start_letter, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)


class AddressAPIViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def recently_updated_addresses(self, request):
        recently_updated_addresses = Address.objects.order_by('-last_update')[:3]
        serialized_data = self.get_serializer(recently_updated_addresses, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def addresses_in_specific_city(self, request):
        # Masalan, "Tashkent" shahridagi manzillar
        city_name = "Tashkent"
        addresses_in_specific_city = Address.objects.filter(city__name=city_name)[:3]
        serialized_data = self.get_serializer(addresses_in_specific_city, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def addresses_starting_with_letter(self, request):
        # "A" harfiga boshlangan manzillar
        letter = "A"
        addresses_starting_with_letter = Address.objects.filter(name__istartswith=letter)[:3]
        serialized_data = self.get_serializer(addresses_starting_with_letter, many=True).data
        return Response(serialized_data)



class CommentsAPIViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('comment', 'comment__users__first_name', 'comment__users__last_name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def comments_by_date(self, request):
        comments_by_date = Comments.objects.order_by('-create_date')[:5]
        serialized_data = self.get_serializer(comments_by_date, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def comments_without_users(self, request):
        comments_without_users = Comments.objects.filter(users__isnull=True)[:5]
        serialized_data = self.get_serializer(comments_without_users, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def recent_comments_of_users(self, request):
        recent_comments_of_users = Comments.objects.order_by('users__last_update')[:5]
        serialized_data = self.get_serializer(recent_comments_of_users, many=True).data
        return Response(serialized_data)



class TestimonialsAPIViewSet(ModelViewSet):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('client_name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def testimonials_without_image(self, request):
        testimonials_without_image = Testimonials.objects.filter(image__isnull=True)[:5]
        serialized_data = self.get_serializer(testimonials_without_image, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def recent_testimonials(self, request):
        recent_testimonials = Testimonials.objects.order_by('-id')[:5]
        serialized_data = self.get_serializer(recent_testimonials, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def testimonials_with_content_length(self, request):
        testimonials_with_content_length = Testimonials.objects.annotate(content_length=Length('content')).order_by(
            '-content_length')[:5]
        serialized_data = self.get_serializer(testimonials_with_content_length, many=True).data
        return Response(serialized_data)
