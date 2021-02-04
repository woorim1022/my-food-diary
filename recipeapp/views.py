from django.shortcuts import render

# Create your views here.
from frame.recipeapp.recipeapp_userdb import User_IngrDb


def recipe(request):
    user_ingrlist = User_IngrDb().select();
    context = {
        'user_ingrlist': user_ingrlist,
    }
    return render(request, 'recipeapp/recipe.html', context);


def recipe_detail(request):
    return render(request, 'recipeapp/recipe_detail.html')