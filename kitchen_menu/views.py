from django.shortcuts import render, get_object_or_404
from .models import Menu

# Create your views here.
def details(request, pk):
    dish = get_object_or_404(Menu, pk = pk)
    context = {
        'dish' : dish,
    }

    return render(request, 'details.html', context)