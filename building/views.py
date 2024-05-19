from django.shortcuts import render
from django.views import View
from .models import Build


class HouseListView(View):
    def get(self, request):
        buildings = Build.objects.all()
        context = {
            "buildings": buildings,
        }
        return render(request, "main/property-grid.html", context)


class HouseDetailView(View):
    def get(self, request, id):
        building = Build.objects.get(id=id)
        context = {
            'building': building
        }
        return render(request, 'main/property-single.html', context)
