from django.shortcuts import render
from django.http import Http404

from .models import Recipe


def index(request):
    latest_recipe_list = Recipe.objects.order_by('-date_published')[:5]
    context = {
        'latest_recipe_list': latest_recipe_list
    }
    return render(request, 'recipes/index.html', context)


def recipe_details(request, recipe_name):
    try:
        recipe = Recipe.objects.get(name=recipe_name)
    except Recipe.DoesNotExist:
        raise Http404('Recipe not found.')

    ingredient_requirements = recipe.ingredientrequirement_set.all()
    context = dict()
    context['recipe'] = recipe
    context['ingredient_requirements'] = ingredient_requirements
    return render(request, 'recipes/detail.html', context)
