from django.shortcuts import render

# Create your views here.
def recipe(request):
    return render(request, 'recipeapp/recipe.html')



def recipe_detail(request):
    return render(request, 'recipeapp/recipe_detail.html')