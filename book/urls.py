from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me),
    path('my_favourite_writers/', views.my_favourite_writers),
    path('sayings_of_great_poets/', views.sayings_of_great_poets),
    path('books/', views.book_list_view),
    path('books/<int:book_id>/', views.book_detail_view),

]

