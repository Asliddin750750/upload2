from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from main.models import Country
from main.serializers import CountrySerializer


class CountryView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer