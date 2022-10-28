from django.db import models


class Animal(models.Model):
    name = models.CharField("Nome do Animal", max_length=50)
    predador = models.BooleanField("Predador")
    poisonous = models.BooleanField("Venenoso")
    domestic = models.BooleanField("Doméstico")

    def __str__(self):
        return self.name
