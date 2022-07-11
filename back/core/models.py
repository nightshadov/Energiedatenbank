from django.db import models
from django.utils import timezone


# Create your models here.


class EnergySource(models.Model):
    name = models.CharField(primary_key=True, max_length=30)

class Year(models.Model):
    year = models.IntegerField(primary_key=True)


class Application(models.Model):
    name = models.CharField(primary_key=True, max_length=30)

class Sector(models.Model):
    name = models.CharField(primary_key=True, max_length=30)

class charTable(models.Model):
    id = models.AutoField(primary_key=True)
    categoryA = models.CharField(max_length=30, unique=True)
    categoryB = models.CharField(max_length=30, unique=True)
    value = models.FloatField(blank=True, null=True)

class FloatTable(models.Model):
    id = models.AutoField(primary_key=True)
    categoryA = models.CharField(max_length=30, unique=True)
    categoryB = models.FloatField(unique=True)
    value = models.FloatField(blank=True, null=True)

class EnYear(models.Model):
    en_year = models.AutoField(primary_key=True)
    fk_energy_source = models.ForeignKey(EnergySource,
    models.DO_NOTHING, db_column='name', default=None)
    fk_year = models.ForeignKey(Year, models.DO_NOTHING,
db_column='year', default=None)

    petajoule = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.petajoule}'

    class Meta:
        unique_together = (('fk_energy_source', 'fk_year'),)


