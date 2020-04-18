from django.db import models


class Wines(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=7)
    sale_price = models.CharField(max_length=10)
    img = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.title, self.price)


class People(models.Model):
    text = models.CharField(max_length=500)
    name = models.CharField(max_length=30)
    img = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)
