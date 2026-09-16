from django.shortcuts import render, redirect
from urllib.parse import quote, unquote
from .forms import SettingsForm

ARTWORKS = [
    {
        'id': 1,
        'title': 'Звездная ночь',
        'author': 'Винсент Ван Гог',
        'year': 1889,
        'description': 'Знаменитая картина постимпрессиониста.',
        'image': 'starry_night.jpg'
    },
    {
        'id': 2,
        'title': 'Мона Лиза',
        'author': 'Леонардо да Винчи',
        'year': 1503,
        'description': 'Шедевр эпохи Возрождения.',
        'image': 'mona_lisa.jpg'
    },
    {
        'id': 3,
        'title': 'Крик',
        'author': 'Эдвард Мунк',
        'year': 1893,
        'description': 'Экспрессионистская картина.',
        'image': 'the_scream.jpg'
    }
]

def gallery_view(request):
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'ru')
    last_visited = unquote(request.COOKIES.get('last_visited', '')) or 'Нет данных'

    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            theme = form.cleaned_data['theme']
            language = form.cleaned_data['language']
            
            response = redirect('gallery')
            response.set_cookie('theme', theme, max_age=3600*24*30)
            response.set_cookie('language', language, max_age=3600*24*30)
            response.set_cookie('last_visited', quote('Галерея'), max_age=3600*24*30)
            return response
    else:
        form = SettingsForm(initial={'theme': theme, 'language': language})

    context = {
        'artworks': ARTWORKS,
        'form': form,
        'theme': theme,
        'language': language,
        'last_visited': last_visited,
    }
    return render(request, 'myapp/gallery.html', context)