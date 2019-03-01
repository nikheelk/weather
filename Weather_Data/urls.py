"""Weather_Data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from weather.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^min_temp_of_uk_bulk_upload/$', minTempOfUkBulkUploading),
    url(r'^max_temp_of_uk_bulk_upload/$', maxTempOfUkBulkUploading),
    url(r'^rainfall_of_uk_bulk_upload/$', rainfallOfUkBulkUploading),

    url(r'^min_temp_of_england_bulk_upload/$', minTempOfEnglandBulkUploading),
    url(r'^max_temp_of_england_bulk_upload/$', maxTempOfEnglandBulkUploading),
    url(r'^rainfall_of_england_bulk_upload/$', rainfallOfEnglandBulkUploading),

    url(r'^min_temp_of_scotland_bulk_upload/$', minTempOfScotlandBulkUploading),
    url(r'^max_temp_of_scotland_bulk_upload/$', maxTempOfScotlandBulkUploading),
    url(r'^rainfall_of_scotland_bulk_upload/$', rainfallOfScotlandBulkUploading),

    url(r'^min_temp_of_wales_bulk_upload/$', minTempOfWalesBulkUploading),
    url(r'^max_temp_of_wales_bulk_upload/$', maxTempOfWalesBulkUploading),
    url(r'^rainfall_of_wales_bulk_upload/$', rainfallOfWalesBulkUploading),

    url(r'^get_list_of_min_temp_of_uk/$', MinTempOfUkListAPIView.as_view()),
    url(r'^get_list_of_max_temp_of_uk/$', MaxTempOfUkListAPIView.as_view()),
    url(r'^get_list_of_rainfall_of_uk/$', RainfallOfUkListAPIView.as_view()),

    url(r'^get_list_of_min_temp_of_england/$', MinTempOfEnglandListAPIView.as_view()),
    url(r'^get_list_of_max_temp_of_england/$', MaxTempOfEnglandListAPIView.as_view()),
    url(r'^get_list_of_rainfall_of_england/$', RainfallOfEnglandListAPIView.as_view()),

    url(r'^get_list_of_min_temp_of_scotland/$', MinTempOfScotlandListAPIView.as_view()),
    url(r'^get_list_of_max_temp_of_scotland/$', MaxTempOfScotlandListAPIView.as_view()),
    url(r'^get_list_of_rainfall_of_scotland/$', RainfallOfScotlandListAPIView.as_view()),

    url(r'^get_list_of_min_temp_of_wales/$', MinTempOfWalesListAPIView.as_view()),
    url(r'^get_list_of_max_temp_of_wales/$', MaxTempOfWalesListAPIView.as_view()),
    url(r'^get_list_of_rainfall_of_wales/$', RainfallOfWalesListAPIView.as_view()),

]
