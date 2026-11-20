from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)  # музей, конный тур, театр

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    place = models.OneToOneField(Place, on_delete=models.CASCADE)  # 1 к 1

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)  # Активный, Спокойный, Семейный

    def __str__(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    categories = models.ManyToManyField(Category)  # многие ко многим

    def __str__(self):
        return self.title


class Comment(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)  # 1 ко многим
    author = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.author