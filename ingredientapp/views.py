from django.shortcuts import render



def ingredient(request):
    return render(request, 'ingredientapp/ingredient.html');


def ingredient_reg(request):
    return render(request, 'ingredientapp/ingredient_reg.html');