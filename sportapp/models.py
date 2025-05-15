from django.db import models


# Create your models here.

class Supplement(models.Model):
    SUPPLEMENT_CATEGORY = [
        ('protein', 'Proteins'),
        ('vitamins', 'Vitamins'),
        ('creatine', 'Creatines'),
        ('aminoacids', 'Aminoacids'),
        ('preworkout', 'Pre-Workout')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='data/')
    code = models.CharField(max_length=10)
    manufacturer = models.CharField(max_length=100)
    isAvailable = models.BooleanField(default=False)
    price = models.IntegerField()
    category = models.CharField(max_length=100, choices=SUPPLEMENT_CATEGORY)
    description = models.TextField(default="Описот не е достапен")

    def __str__(self):
        return self.name + " " + self.manufacturer
