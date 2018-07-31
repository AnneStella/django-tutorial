from django.db import models


class Destination(models.Model):
    place = models.CharField(max_length=128)
    place_logo = models.CharField(max_length=472)
    continent = models.CharField(max_length=200)
    tribe = models.CharField(max_length=300)
    language = models.charField(max_length=150)


class Place(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=125)
    place_name = models.CharField(max_length=902)
