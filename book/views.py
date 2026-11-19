from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.shortcuts import render, get_object_or_404





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

def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})


def book_detail_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/book_detail.html', {'book': book})
