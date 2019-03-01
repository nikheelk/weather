from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(MinTempOfUk)
class MinTempOfUkAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'value', 'year', 'month')


@admin.register(MaxTempOfUk)
class MaxTempOfUkAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'value', 'year', 'month')


@admin.register(RainfallOfUk)
class RainfallOfUkAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'value', 'year', 'month')


@admin.register(MinTempOfEngland)
class MinTempOfEnglandAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'value', 'year', 'month')


@admin.register(MaxTempOfEngland)
class MaxTempOfEnglandAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'value', 'year', 'month')


@admin.register(RainfallOfEngland)
class RainfallOfEnglandAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'value', 'year', 'month')


@admin.register(MinTempOfScotland)
class MinTempOfScotlandAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'value', 'year', 'month')


@admin.register(MaxTempOfScotland)
class MaxTempOfScotlandAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'value', 'year', 'month')


@admin.register(RainfallOfScotland)
class RainfallOfScotlandAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'value', 'year', 'month')


@admin.register(MinTempOfWales)
class MinTempOfWalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'value', 'year', 'month')


@admin.register(MaxTempOfWales)
class MaxTempOfWalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'value', 'year', 'month')


@admin.register(RainfallOfWales)
class RainfallOfWalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'value', 'year', 'month')