from django.db import models

from .validators import validate_musician_name_start_from_capital


class Musician(models.Model):
    name = models.CharField(max_length=100,
                            validators=[validate_musician_name_start_from_capital])

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.PROTECT)
    date_release = models.DateField()
    track = models.ManyToManyField('Track', related_name='tracks')

    def __str__(self):
        return f'Album {self.title} of {self.musician}'


class Track(models.Model):
    album = models.ManyToManyField(Album, related_name='albums')
    title = models.CharField(max_length=100)
    serial_number = models.SmallIntegerField()

    def __str__(self):
        return self.title
