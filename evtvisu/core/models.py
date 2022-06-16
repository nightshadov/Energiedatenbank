from django.db import models
from django.utils import timezone


# Create your models here.


class EnergySource(models.Model):
    energy_source_id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=30)

class Year(models.Model):
    year_id = models.IntegerField(primary_key=True)


class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=30)

class Sector(models.Model):
    sector_id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=30)

class EnYear(models.Model):
    en_year_id = models.AutoField(primary_key=True)
    fk_energy_source_id = models.ForeignKey(EnergySource,
    models.DO_NOTHING, db_column='energy_source_id')
    fk_year_id = models.ForeignKey(Year, models.DO_NOTHING,
db_column='year_id')

    petajoule = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.petajoule}'

    class Meta:
        unique_together = (('fk_energy_source_id', 'fk_year_id'),)


