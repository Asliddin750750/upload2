from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from file3.models import Notebook
from file3.serializers import NotebookSerializer


class NotebookView(ListCreateAPIView):
    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()

    def list(self, request, *args, **kwargs):
        result = super().list(request, *args, **kwargs)
        return Response({
            'notebooks': result.data
        })
