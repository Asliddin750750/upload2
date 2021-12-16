import os
import datetime
import random

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import transaction
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from upload.models import Car
from upload.serializers import CarSerializer


class UploadFileView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({
                "file": "File not found"
            }, status=status.HTTP_200_OK)

        with transaction.atomic():
            filename, extension = os.path.splitext(file.name)
            name = "{:%Y-%m-%d-%H-%M-%S-%f}-{}{}".format(datetime.datetime.now(),
                                                         random.randint(10000, 99999), extension.lower())

            dirname = "media/images/"

            if not os.path.isdir(dirname):
                os.makedirs(dirname, exist_ok=True)

            file_path = dirname + name

            with open(file_path, "wb+") as f:
                for chunk in file.chunks():
                    f.write(chunk)

            obj = Car.objects.create(
                brand=request.data.get('brand'),
                dirname=dirname,
                name=name,
                filename=file.name,
                extension=extension[1:].lower(),
                mimetype=file.content_type
            )

            return Response({
                "id": obj.id
            }, status=status.HTTP_200_OK)


class FilesView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response({
            'success': True,
            'car': serializer.data
        }, status=status.HTTP_200_OK)


class FileResponseView(APIView):
    def get(self, request):
        fs = FileSystemStorage('../images/')
        response = FileResponse(fs.open('2021-12-11-06-13-48-249559-46484.jpeg', 'rb'), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="filename.pdf"'
        return response
