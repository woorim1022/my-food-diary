from django.shortcuts import render

# Create your views here.
from frame.recipeapp.recipeapp_userdb import RecipeDb


def recipe(request):
    recipe = RecipeDb().select();
    context = {
        'recipes': recipe,
    }
    return render(request, 'recipeapp/recipe.html', context);


def recipe_detail(request):
    recipe = RecipeDb().select();
    context = {
        'recipe_detail': recipe,
    }
    return render(request, 'recipeapp/recipe_detail.html', context)