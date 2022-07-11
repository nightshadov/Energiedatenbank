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

class EnYearSect(models.Model):
    en_year_sect = models.AutoField(primary_key=True)
    fk_energy_source = models.ForeignKey(EnergySource,
    models.DO_NOTHING, db_column='EnergieTräger', default=None)
    fk_year = models.ForeignKey(Year, models.DO_NOTHING,
db_column='Jahr', default=None)
    fk_sector = models.ForeignKey(Sector,
                                         models.DO_NOTHING, db_column='Sektor', default=None)

    petajoule = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.petajoule}'

    class Meta:
        unique_together = (('fk_energy_source', 'fk_year','fk_sector'),)


class EnYearAppl(models.Model):
    en_year_sect = models.AutoField(primary_key=True)
    fk_energy_source = models.ForeignKey(EnergySource,models.DO_NOTHING, db_column='EnergieTräger', default=None)

    fk_year = models.ForeignKey(Year, models.DO_NOTHING,db_column='Jahr', default=None)

    fk_application = models.ForeignKey(Application, models.DO_NOTHING, db_column='Anwendung', default=None)

    petajoule = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.petajoule}'

    class Meta:
        unique_together = (('fk_energy_source', 'fk_year','fk_application'),)


class EnYearSectAppl(models.Model):
    en_year_sect = models.AutoField(primary_key=True, verbose_name='ID')
    fk_energy_source = models.ForeignKey(EnergySource,models.DO_NOTHING, db_column='EnergieTräger', verbose_name="EnergieTräger", default=None)

    fk_year = models.ForeignKey(Year, models.DO_NOTHING,db_column='Jahr', verbose_name='Jahr' , default=None)

    fk_application = models.ForeignKey(Application, models.DO_NOTHING, db_column='Anwendung', verbose_name='Anwendung' , default=None)

    fk_sector = models.ForeignKey(Sector, models.DO_NOTHING, db_column='Sektor', verbose_name='Sektor' , default=None)

    petajoule = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.petajoule}'

    class Meta:
        unique_together = (('fk_energy_source', 'fk_year','fk_application','fk_sector'),)



class Sample(models.Model):
    username = models.CharField(max_length=30)
    identifier = models.IntegerField(primary_key=True,)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

class Sample2(models.Model):
    identifier = models.IntegerField(primary_key=True)
    accessCode = models.CharField(max_length=30)
    recCode = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

