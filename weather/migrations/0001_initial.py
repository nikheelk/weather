# Generated by Django 2.1.1 on 2019-02-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaxTempOfEngland',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('uk', 'UK'), ('england', 'England'), ('scotland', 'Scotland'), ('wales', 'Wales')], default='england', max_length=10)),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('year', models.IntegerField(blank=True, default=None, null=True)),
                ('month', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Tmax Of England',
                'verbose_name_plural': 'Tmax Of England',
                'db_table': 'max_temp_england',
            },
        ),
        migrations.CreateModel(
            name='MaxTempOfScotland',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('uk', 'UK'), ('england', 'England'), ('scotland', 'Scotland'), ('wales', 'Wales')], default='scotland', max_length=10)),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('year', models.IntegerField(blank=True, default=None, null=True)),
                ('month', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Tmax Of Scotland',
                'verbose_name_plural': 'Tmax Of Scotland',
                'db_table': 'max_temp_scotland',
            },
        ),
        migrations.CreateModel(
            name='MaxTempOfUk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('uk', 'UK'), ('england', 'England'), ('scotland', 'Scotland'), ('wales', 'Wales')], default='uk', max_length=10)),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('year', models.IntegerField(blank=True, default=None, null=True)),
                ('month', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Tmax Of UK',
                'verbose_name_plural': 'Tmax Of UK',
                'db_table': 'max_temp_uk',
            },
        ),
        migrations.CreateModel(
            name='MaxTempOfWales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('uk', 'UK'), ('england', 'England'), ('scotland', 'Scotland'), ('wales', 'Wales')], default='wales', max_length=10)),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('year', models.IntegerField(blank=True, default=None, null=True)),
                ('month', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Tmax Of Wales',
                'verbose_name_plural': 'Tmax Of Wales',
                'db_table': 'max_temp_wales',
            },
        ),
        migrations.CreateModel(
            name='MinTempOfEngland',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('uk', 'UK'), ('england', 'England'), ('scotland', 'Scotland'), ('wales', 'Wales')], default='england', max_length=10)),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('year', models.IntegerField(blank=True, default=None, null=True)),
                ('month', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Tmin Of England',
                'verbose_name_plural': 'Tmin Of England',
                'db_table': 'min_temp_england',
            },
        ),
        migrations.CreateModel(
            name='MinTempOfScotland',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('uk', 'UK'), ('england', 'England'), ('scotland', 'Scotland'), ('wales', 'Wales')], default='scotland', max_length=10)),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('year', models.IntegerField(blank=True, default=None, null=True)),
                ('month', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Tmin Of Scotland',
                'verbose_name_plural': 'Tmin Of Scotland',
                'db_table': 'min_temp_scotland',
            },
        ),
        migrations.CreateModel(
            name='MinTempOfUk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('uk', 'UK'), ('england', 'England'), ('scotland', 'Scotland'), ('wales', 'Wales')], default='uk', max_length=10)),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('year', models.IntegerField(blank=True, default=None, null=True)),
                ('month', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Tmin Of UK',
                'verbose_name_plural': 'Tmin Of UK',
                'db_table': 'min_temp_uk',
            },
        ),
        migrations.CreateModel(
            name='MinTempOfWales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('uk', 'UK'), ('england', 'England'), ('scotland', 'Scotland'), ('wales', 'Wales')], default='wales', max_length=10)),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('year', models.IntegerField(blank=True, default=None, null=True)),
                ('month', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Tmin Of Wales',
                'verbose_name_plural': 'Tmin Of Wales',
                'db_table': 'min_temp_wales',
            },
        ),
        migrations.CreateModel(
            name='RainfallOfEngland',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('uk', 'UK'), ('england', 'England'), ('scotland', 'Scotland'), ('wales', 'Wales')], default='england', max_length=10)),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('year', models.IntegerField(blank=True, default=None, null=True)),
                ('month', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Rainfall Of England',
                'verbose_name_plural': 'Rainfall Of England',
                'db_table': 'rainfall_england',
            },
        ),
        migrations.CreateModel(
            name='RainfallOfScotland',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('uk', 'UK'), ('england', 'England'), ('scotland', 'Scotland'), ('wales', 'Wales')], default='scotland', max_length=10)),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('year', models.IntegerField(blank=True, default=None, null=True)),
                ('month', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Rainfall Of Scotland',
                'verbose_name_plural': 'Rainfall Of Scotland',
                'db_table': 'rainfall_scotland',
            },
        ),
        migrations.CreateModel(
            name='RainfallOfUk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('uk', 'UK'), ('england', 'England'), ('scotland', 'Scotland'), ('wales', 'Wales')], default='uk', max_length=10)),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('year', models.IntegerField(blank=True, default=None, null=True)),
                ('month', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Rainfall Of UK',
                'verbose_name_plural': 'Rainfall Of UK',
                'db_table': 'rainfall_uk',
            },
        ),
        migrations.CreateModel(
            name='RainfallOfWales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('uk', 'UK'), ('england', 'England'), ('scotland', 'Scotland'), ('wales', 'Wales')], default='wales', max_length=10)),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('year', models.IntegerField(blank=True, default=None, null=True)),
                ('month', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Rainfall Of Wales',
                'verbose_name_plural': 'Rainfall Of Wales',
                'db_table': 'rainfall_wales',
            },
        ),
    ]
