from django.db import models
from weather.constants import *

# Create your models here.


class MinTempOfUk(models.Model):
    LOCATIONS = (
        ("uk", LocationMaster.uk.value),
        ("england", LocationMaster.england.value),
        ("scotland", LocationMaster.scotland.value),
        ("wales", LocationMaster.wales.value),
    )
    location = models.CharField(choices=LOCATIONS, default="uk", max_length=10)
    value = models.FloatField(blank=True, null=True, default=None)
    year = models.IntegerField(blank=True, null=True, default=None)
    month = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'min_temp_uk'
        verbose_name = "Tmin Of UK"
        verbose_name_plural = "Tmin Of UK"


class MaxTempOfUk(models.Model):
    LOCATIONS = (
        ("uk", LocationMaster.uk.value),
        ("england", LocationMaster.england.value),
        ("scotland", LocationMaster.scotland.value),
        ("wales", LocationMaster.wales.value),
    )
    location = models.CharField(choices=LOCATIONS, default="uk", max_length=10)
    value = models.FloatField(blank=True, null=True, default=None)
    year = models.IntegerField(blank=True, null=True, default=None)
    month = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'max_temp_uk'
        verbose_name = "Tmax Of UK"
        verbose_name_plural = "Tmax Of UK"


class RainfallOfUk(models.Model):
    LOCATIONS = (
        ("uk", LocationMaster.uk.value),
        ("england", LocationMaster.england.value),
        ("scotland", LocationMaster.scotland.value),
        ("wales", LocationMaster.wales.value),
    )
    location = models.CharField(choices=LOCATIONS, default="uk", max_length=10)
    value = models.FloatField(blank=True, null=True, default=None)
    year = models.IntegerField(blank=True, null=True, default=None)
    month = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'rainfall_uk'
        verbose_name = "Rainfall Of UK"
        verbose_name_plural = "Rainfall Of UK"


class MinTempOfEngland(models.Model):
    LOCATIONS = (
        ("uk", LocationMaster.uk.value),
        ("england", LocationMaster.england.value),
        ("scotland", LocationMaster.scotland.value),
        ("wales", LocationMaster.wales.value),
    )
    location = models.CharField(choices=LOCATIONS, default="england", max_length=10)
    value = models.FloatField(blank=True, null=True, default=None)
    year = models.IntegerField(blank=True, null=True, default=None)
    month = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'min_temp_england'
        verbose_name = "Tmin Of England"
        verbose_name_plural = "Tmin Of England"


class MaxTempOfEngland(models.Model):
    LOCATIONS = (
        ("uk", LocationMaster.uk.value),
        ("england", LocationMaster.england.value),
        ("scotland", LocationMaster.scotland.value),
        ("wales", LocationMaster.wales.value),
    )
    location = models.CharField(choices=LOCATIONS, default="england", max_length=10)
    value = models.FloatField(blank=True, null=True, default=None)
    year = models.IntegerField(blank=True, null=True, default=None)
    month = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'max_temp_england'
        verbose_name = "Tmax Of England"
        verbose_name_plural = "Tmax Of England"


class RainfallOfEngland(models.Model):
    LOCATIONS = (
        ("uk", LocationMaster.uk.value),
        ("england", LocationMaster.england.value),
        ("scotland", LocationMaster.scotland.value),
        ("wales", LocationMaster.wales.value),
    )
    location = models.CharField(choices=LOCATIONS, default="england", max_length=10)
    value = models.FloatField(blank=True, null=True, default=None)
    year = models.IntegerField(blank=True, null=True, default=None)
    month = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'rainfall_england'
        verbose_name = "Rainfall Of England"
        verbose_name_plural = "Rainfall Of England"


class MinTempOfScotland(models.Model):
    LOCATIONS = (
        ("uk", LocationMaster.uk.value),
        ("england", LocationMaster.england.value),
        ("scotland", LocationMaster.scotland.value),
        ("wales", LocationMaster.wales.value),
    )
    location = models.CharField(choices=LOCATIONS, default="scotland", max_length=10)
    value = models.FloatField(blank=True, null=True, default=None)
    year = models.IntegerField(blank=True, null=True, default=None)
    month = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'min_temp_scotland'
        verbose_name = "Tmin Of Scotland"
        verbose_name_plural = "Tmin Of Scotland"


class MaxTempOfScotland(models.Model):
    LOCATIONS = (
        ("uk", LocationMaster.uk.value),
        ("england", LocationMaster.england.value),
        ("scotland", LocationMaster.scotland.value),
        ("wales", LocationMaster.wales.value),
    )
    location = models.CharField(choices=LOCATIONS, default="scotland", max_length=10)
    value = models.FloatField(blank=True, null=True, default=None)
    year = models.IntegerField(blank=True, null=True, default=None)
    month = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'max_temp_scotland'
        verbose_name = "Tmax Of Scotland"
        verbose_name_plural = "Tmax Of Scotland"


class RainfallOfScotland(models.Model):
    LOCATIONS = (
        ("uk", LocationMaster.uk.value),
        ("england", LocationMaster.england.value),
        ("scotland", LocationMaster.scotland.value),
        ("wales", LocationMaster.wales.value),
    )
    location = models.CharField(choices=LOCATIONS, default="scotland", max_length=10)
    value = models.FloatField(blank=True, null=True, default=None)
    year = models.IntegerField(blank=True, null=True, default=None)
    month = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'rainfall_scotland'
        verbose_name = "Rainfall Of Scotland"
        verbose_name_plural = "Rainfall Of Scotland"


class MinTempOfWales(models.Model):
    LOCATIONS = (
        ("uk", LocationMaster.uk.value),
        ("england", LocationMaster.england.value),
        ("scotland", LocationMaster.scotland.value),
        ("wales", LocationMaster.wales.value),
    )
    location = models.CharField(choices=LOCATIONS, default="wales", max_length=10)
    value = models.FloatField(blank=True, null=True, default=None)
    year = models.IntegerField(blank=True, null=True, default=None)
    month = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'min_temp_wales'
        verbose_name = "Tmin Of Wales"
        verbose_name_plural = "Tmin Of Wales"


class MaxTempOfWales(models.Model):
    LOCATIONS = (
        ("uk", LocationMaster.uk.value),
        ("england", LocationMaster.england.value),
        ("scotland", LocationMaster.scotland.value),
        ("wales", LocationMaster.wales.value),
    )
    location = models.CharField(choices=LOCATIONS, default="wales", max_length=10)
    value = models.FloatField(blank=True, null=True, default=None)
    year = models.IntegerField(blank=True, null=True, default=None)
    month = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'max_temp_wales'
        verbose_name = "Tmax Of Wales"
        verbose_name_plural = "Tmax Of Wales"


class RainfallOfWales(models.Model):
    LOCATIONS = (
        ("uk", LocationMaster.uk.value),
        ("england", LocationMaster.england.value),
        ("scotland", LocationMaster.scotland.value),
        ("wales", LocationMaster.wales.value),
    )
    location = models.CharField(choices=LOCATIONS, default="wales", max_length=10)
    value = models.FloatField(blank=True, null=True, default=None)
    year = models.IntegerField(blank=True, null=True, default=None)
    month = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'rainfall_wales'
        verbose_name = "Rainfall Of Wales"
        verbose_name_plural = "Rainfall Of Wales"
