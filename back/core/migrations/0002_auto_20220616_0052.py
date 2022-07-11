# Generated by Django 3.2.3 on 2022-06-16 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('application_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnergySource',
            fields=[
                ('energy_source_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnYear',
            fields=[
                ('en_year_id', models.AutoField(primary_key=True, serialize=False)),
                ('petajoule', models.FloatField(blank=True, null=True)),
                ('fk_energy_source_id', models.ForeignKey(db_column='energy_source_id', on_delete=django.db.models.deletion.DO_NOTHING, to='core.energysource')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('sector_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('year_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='AlmemoLog',
        ),
        migrations.DeleteModel(
            name='ExperimentLog',
        ),
        migrations.AddField(
            model_name='enyear',
            name='fk_year_id',
            field=models.ForeignKey(db_column='year_id', on_delete=django.db.models.deletion.DO_NOTHING, to='core.year'),
        ),
        migrations.AlterUniqueTogether(
            name='enyear',
            unique_together={('fk_energy_source_id', 'fk_year_id')},
        ),
    ]