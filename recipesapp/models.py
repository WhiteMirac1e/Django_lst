from django.db import models

# Create your models here.
# recipes/models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps_cooking = models.TextField()
    time_for_cooking = models.TimeField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Рецепты'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipes-detail', kwargs={'pk': self.pk})