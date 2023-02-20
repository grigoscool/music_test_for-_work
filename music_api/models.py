from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.PROTECT)
    date_release = models.DateField()

    def __str__(self):
        return f'Album {self.title} of {self.musician}'


class Track(models.Model):
    album = models.ForeignKey(
        Album, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=100)
    serial_number = models.SmallIntegerField()

    def __str__(self):
        return self.title
