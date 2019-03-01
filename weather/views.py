from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework import status
import urllib.request as ur
import json

# Create your views here.


@api_view(['GET', 'POST'])
def minTempOfUkBulkUploading(request):
    url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Tmin-UK.json"
    response = ur.urlopen(url)
    data = json.loads(response.read())
    many = isinstance(data, list)
    # data = request.data
    obj = data
    result_data = []
    if many:
        if len(obj) > 0:
            for i in range(0, len(obj)):
                uk_serializer = MinTempOfUkSerializer(data=obj[i])

                if uk_serializer.is_valid():
                    uk_serializer.save()
                else:
                    return Response(uk_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid data. Expected a list , but got dictionary.", status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def maxTempOfUkBulkUploading(request):
    url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Tmax-UK.json"
    response = ur.urlopen(url)
    data = json.loads(response.read())
    many = isinstance(data, list)
    # data = request.data
    obj = data
    result_data = []
    if many:
        if len(obj) > 0:
            for i in range(0, len(obj)):
                uk_serializer = MaxTempOfUkSerializer(data=obj[i])

                if uk_serializer.is_valid():
                    uk_serializer.save()
                else:
                    return Response(uk_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid data. Expected a list , but got dictionary.", status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def rainfallOfUkBulkUploading(request):
    url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Rainfall-UK.json"
    response = ur.urlopen(url)
    data = json.loads(response.read())
    many = isinstance(data, list)
    # data = request.data
    obj = data
    result_data = []
    if many:
        if len(obj) > 0:
            for i in range(0, len(obj)):
                uk_serializer = RainfallOfUkSerializer(data=obj[i])

                if uk_serializer.is_valid():
                    uk_serializer.save()
                else:
                    return Response(uk_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid data. Expected a list , but got dictionary.", status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def minTempOfEnglandBulkUploading(request):
    url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Tmin-England.json"
    response = ur.urlopen(url)
    data = json.loads(response.read())
    many = isinstance(data, list)
    # data = request.data
    obj = data
    result_data = []
    if many:
        if len(obj) > 0:
            for i in range(0, len(obj)):
                england_serializer = MinTempOfEnglandSerializer(data=obj[i])

                if england_serializer.is_valid():
                    england_serializer.save()
                else:
                    return Response(england_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid data. Expected a list , but got dictionary.", status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def maxTempOfEnglandBulkUploading(request):
    url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Tmax-England.json"
    response = ur.urlopen(url)
    data = json.loads(response.read())
    many = isinstance(data, list)
    # data = request.data
    obj = data
    result_data = []
    if many:
        if len(obj) > 0:
            for i in range(0, len(obj)):
                england_serializer = MaxTempOfEnglandSerializer(data=obj[i])

                if england_serializer.is_valid():
                    england_serializer.save()
                else:
                    return Response(england_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid data. Expected a list , but got dictionary.", status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def rainfallOfEnglandBulkUploading(request):
    url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Rainfall-England.json"
    response = ur.urlopen(url)
    data = json.loads(response.read())
    many = isinstance(data, list)
    # data = request.data
    obj = data
    result_data = []
    if many:
        if len(obj) > 0:
            for i in range(0, len(obj)):
                england_serializer = RainfallOfEnglandSerializer(data=obj[i])

                if england_serializer.is_valid():
                    england_serializer.save()
                else:
                    return Response(england_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid data. Expected a list , but got dictionary.", status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def minTempOfScotlandBulkUploading(request):
    url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Tmin-Scotland.json"
    response = ur.urlopen(url)
    data = json.loads(response.read())
    many = isinstance(data, list)
    # data = request.data
    obj = data
    result_data = []
    if many:
        if len(obj) > 0:
            for i in range(0, len(obj)):
                scotland_serializer = MinTempOfScotlandSerializer(data=obj[i])

                if scotland_serializer.is_valid():
                    scotland_serializer.save()
                else:
                    return Response(scotland_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid data. Expected a list , but got dictionary.", status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def maxTempOfScotlandBulkUploading(request):
    url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Tmax-Scotland.json"
    response = ur.urlopen(url)
    data = json.loads(response.read())
    many = isinstance(data, list)
    # data = request.data
    obj = data
    result_data = []
    if many:
        if len(obj) > 0:
            for i in range(0, len(obj)):
                scotland_serializer = MaxTempOfScotlandSerializer(data=obj[i])

                if scotland_serializer.is_valid():
                    scotland_serializer.save()
                else:
                    return Response(scotland_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid data. Expected a list , but got dictionary.", status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def rainfallOfScotlandBulkUploading(request):
    url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Rainfall-Scotland.json"
    response = ur.urlopen(url)
    data = json.loads(response.read())
    many = isinstance(data, list)
    # data = request.data
    obj = data
    result_data = []
    if many:
        if len(obj) > 0:
            for i in range(0, len(obj)):
                scotland_serializer = RainfallOfScotlandSerializer(data=obj[i])

                if scotland_serializer.is_valid():
                    scotland_serializer.save()
                else:
                    return Response(scotland_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid data. Expected a list , but got dictionary.", status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def minTempOfWalesBulkUploading(request):
    url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Tmin-Wales.json"
    response = ur.urlopen(url)
    data = json.loads(response.read())
    many = isinstance(data, list)
    # data = request.data
    obj = data
    result_data = []
    if many:
        if len(obj) > 0:
            for i in range(0, len(obj)):
                wales_serializer = MinTempOfWalesSerializer(data=obj[i])

                if wales_serializer.is_valid():
                    wales_serializer.save()
                else:
                    return Response(wales_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid data. Expected a list , but got dictionary.", status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def maxTempOfWalesBulkUploading(request):
    url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Tmax-Wales.json"
    response = ur.urlopen(url)
    data = json.loads(response.read())
    many = isinstance(data, list)
    # data = request.data
    obj = data
    result_data = []
    if many:
        if len(obj) > 0:
            for i in range(0, len(obj)):
                wales_serializer = MaxTempOfWalesSerializer(data=obj[i])

                if wales_serializer.is_valid():
                    wales_serializer.save()
                else:
                    return Response(wales_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid data. Expected a list , but got dictionary.", status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def rainfallOfWalesBulkUploading(request):
    url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Rainfall-Wales.json"
    response = ur.urlopen(url)
    data = json.loads(response.read())
    many = isinstance(data, list)
    # data = request.data
    obj = data
    result_data = []
    if many:
        if len(obj) > 0:
            for i in range(0, len(obj)):
                wales_serializer = RainfallOfWalesSerializer(data=obj[i])

                if wales_serializer.is_valid():
                    wales_serializer.save()
                else:
                    return Response(wales_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Invalid data. Expected a list , but got dictionary.", status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_201_CREATED)


class MinTempOfUkListAPIView(ListAPIView):
    queryset = MinTempOfUk.objects.all()
    serializer_class = MinTempOfUkSerializer


class MaxTempOfUkListAPIView(ListAPIView):
    queryset = MaxTempOfUk.objects.all()
    serializer_class = MaxTempOfUkSerializer


class RainfallOfUkListAPIView(ListAPIView):
    queryset = RainfallOfUk.objects.all()
    serializer_class = RainfallOfUkSerializer


class MinTempOfEnglandListAPIView(ListAPIView):
    queryset = MinTempOfEngland.objects.all()
    serializer_class = MinTempOfEnglandSerializer


class MaxTempOfEnglandListAPIView(ListAPIView):
    queryset = MaxTempOfEngland.objects.all()
    serializer_class = MaxTempOfEnglandSerializer


class RainfallOfEnglandListAPIView(ListAPIView):
    queryset = RainfallOfEngland.objects.all()
    serializer_class = RainfallOfEnglandSerializer


class MinTempOfScotlandListAPIView(ListAPIView):
    queryset = MinTempOfScotland.objects.all()
    serializer_class = MinTempOfScotlandSerializer


class MaxTempOfScotlandListAPIView(ListAPIView):
    queryset = MaxTempOfScotland.objects.all()
    serializer_class = MaxTempOfScotlandSerializer


class RainfallOfScotlandListAPIView(ListAPIView):
    queryset = RainfallOfScotland.objects.all()
    serializer_class = RainfallOfScotlandSerializer


class MinTempOfWalesListAPIView(ListAPIView):
    queryset = MinTempOfWales.objects.all()
    serializer_class = MinTempOfWalesSerializer


class MaxTempOfWalesListAPIView(ListAPIView):
    queryset = MaxTempOfWales.objects.all()
    serializer_class = MaxTempOfWalesSerializer


class RainfallOfWalesListAPIView(ListAPIView):
    queryset = RainfallOfWales.objects.all()
    serializer_class = RainfallOfWalesSerializer
