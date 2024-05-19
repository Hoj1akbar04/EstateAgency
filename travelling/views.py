from django.shortcuts import render, redirect
from django.views import View
from .models import Travel


class TravelListView(View):
    def get(self, request):
        travels = Travel.objects.all()
        context = {
            "travels": travels,
        }
        return render(request, "main/blog-grid.html", context)



class TravelDetailView(View):
    def get(self, request, id):
        travel = Travel.objects.get(id=id)
        context = {
            'travel': travel
        }
        return render(request, 'main/blog-single.html', context)