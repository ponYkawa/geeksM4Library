from django.contrib import admin
from .models import Place, Person, Category, Tour, Comment

admin.site.register(Place)
admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Tour)
admin.site.register(Comment)

