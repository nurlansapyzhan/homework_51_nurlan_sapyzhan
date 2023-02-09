from random import randint

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

cat = {
    'name': None,
    'age': 1,
    'happiness': 10,
    'satiety': 40,
    'is_sleeping': False
}


def cat_stats(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'main_page.html')
    else:
        if cat['name'] is None:
            cat['name'] = request.POST.get('name')
        cat_action(request)
        return render(request, 'cat_stats.html',
                      context={'name': cat['name'], 'age': cat.get('age'),
                               'happiness': cat.get('happiness'),
                               'satiety': cat.get('satiety'), 'is_sleeping': cat.get('is_sleeping')})


def cat_action(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'cat_stats.html')
    else:
        if request.POST.get('action') == 'play':
            if cat['is_sleeping']:
                cat['is_sleeping'] = False
                cat['happiness'] -= 5
            else:
                cat['happiness'] += 15
                cat['satiety'] -= 10
                chance = randint(1, 3)
                if chance == 1:
                    cat['happiness'] = 0
        elif request.POST.get('action') == 'feed':
            if cat['is_sleeping']:
                pass
            else:
                cat['satiety'] += 15
                cat['happiness'] += 5
                if cat['satiety'] > 99:
                    cat['happiness'] -= 30
        elif request.POST.get('action') == 'sleep':
            if cat['is_sleeping']:
                pass
            else:
                cat['is_sleeping'] = True
