from django.shortcuts import render
from django.http import HttpResponse


def about_me(request):
    return HttpResponse("<h1>Обо мне</h1><p>Меня зовут Дони, я учусь на Python backend в GEEKS.</p>")


def my_favourite_writers(request):
    return HttpResponse(
        "<h1>Мои любимые писатели</h1>"
        "<p>1. Агата Кристи</p>"
        "<p>2. Эндрю Найдерман</p>"
        "<p>3. Майкл Коннелли</p>"
    )



def sayings_of_great_poets(request):
    return HttpResponse(
        "<h1>Высказывания великих поэтов</h1>"
        "<p>Никто не хочет любить нас в обыновенного человека</p>"
        "<img src='https://www.litres.ru/journal/c/2024/07/nthz6JDjwPk.png'>"
        "<p>Будь собой прочие роли уже заняты</p>"
        "<img src='https://content-management-files.canva.com/be564183-70d3-4428-a533-c455e61ef160/GreatPeoplesQuotesRU5.png' width='300'>"
    )
