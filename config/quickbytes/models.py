from django.db import models

class Byte(models.Model):
    meal_choices=(
        ('Breakfast', 'Breakfast'),
        ('Dinner', 'Dinner'),
        ('Dessert', 'Dessert'),
        ('Drinks','Drinks'),
        ('Snacks', 'Snacks')


    )
    title = models.CharField(max_length=128)
    recipe = models.TextField(default='Remember it should be a short easy recipe with minimal ingredients...')
    image = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=300)
    category = models.CharField(max_length=50, choices=meal_choices)
    author = models.CharField(max_length=128 , blank=False, default='quick byte user')

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.author
    


# Create your models here.
