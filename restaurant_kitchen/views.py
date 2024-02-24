from django.shortcuts import render,redirect
from kitchen_menu.models import Menu, UserFeedback

def home(request):
    starters = Menu.objects.filter(Meal_type = 'starters')
    maincourse = Menu.objects.filter(Meal_type = 'main_course')
    desserts = Menu.objects.filter(Meal_type = 'desserts')
    salads = Menu.objects.filter(Meal_type = 'salads')
    context = {
        'starters' : starters,
        'maincourse' : maincourse,
        'desserts' : desserts,
        'salads' : salads,
    }

    return render(request, 'home.html', context)


def contact(request):
    if request.method == 'POST':
        UserFeedback.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            message = request.POST['message']
        )
        return redirect('home')

    return render(request, 'contact.html')