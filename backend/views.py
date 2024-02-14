from django.shortcuts import render
from backend import models
def index(request):

    return render(request,'backend/index.html',{})


def about(request):
    return render(request, 'backend/about.html', {})

def term_conditions(request):
    return render(request,'backend/term-conditions.html',{})

def privacy_policy(request):
    return render(request,'backend/privacy-policy.html',{})


def restaurant(requests):
    breakfast = models.RestaurantItem.objects.filter(category='Breakfast')
    lunch = models.RestaurantItem.objects.filter(category='Lunch')
    dinner = models.RestaurantItem.objects.filter(category='Dinner')
    drink = models.RestaurantItem.objects.filter(category='Drink')


    context = {
        "breakfast" : breakfast,
        "lunch": lunch,
        "dinner": dinner,
        "drink" : drink,

    }
    return render(requests,'backend/restaurant.html',context)