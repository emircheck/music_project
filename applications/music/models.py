from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    year = models.PositiveIntegerField(default=1850)

    def __str__(self):
        return f'{self.title} -> {self.year}'


class Music(models.Model):
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    year = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='music')

    def __str__(self):
        return f'{self.category.title} -> {self.title}'
