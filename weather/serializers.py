from .models import *
from rest_framework import serializers


class MinTempOfUkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinTempOfUk
        fields = '__all__'


class MaxTempOfUkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaxTempOfUk
        fields = '__all__'


class RainfallOfUkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RainfallOfUk
        fields = '__all__'


class MinTempOfEnglandSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinTempOfEngland
        fields = '__all__'


class MaxTempOfEnglandSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaxTempOfEngland
        fields = '__all__'


class RainfallOfEnglandSerializer(serializers.ModelSerializer):
    class Meta:
        model = RainfallOfEngland
        fields = '__all__'


class MinTempOfScotlandSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinTempOfScotland
        fields = '__all__'


class MaxTempOfScotlandSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaxTempOfScotland
        fields = '__all__'


class RainfallOfScotlandSerializer(serializers.ModelSerializer):
    class Meta:
        model = RainfallOfScotland
        fields = '__all__'


class MinTempOfWalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinTempOfWales
        fields = '__all__'


class MaxTempOfWalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaxTempOfWales
        fields = '__all__'


class RainfallOfWalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RainfallOfWales
        fields = '__all__'
