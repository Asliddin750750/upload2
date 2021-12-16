import datetime
import os
import random

from django.conf import settings
from django.db import transaction
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from file2.models import Phone2
from file2.serializers import PhoneSerializer2


class AddPhoneView2(APIView):
    def post(self, request):
        image = request.FILES.get('image')
        if not image:
            return Response({
                "file": "File not found"
            }, status=status.HTTP_200_OK)

        try:
            print("Size:", image.size)
        except AttributeError as e:
            return Response({"image": str(e)})

        with transaction.atomic():
            filename, extension = os.path.splitext(image.name)
            name = "{:%Y-%m-%d-%H-%M-%S-%f}-{}{}".format(datetime.datetime.now(),
                                                         random.randint(10000, 99999), extension.lower())

            dirname = "phones/"

            if not os.path.isdir(dirname):
                os.makedirs(dirname, exist_ok=True)

            image_path = dirname + name

            with open('media/' + image_path, "wb+") as f:
                for chunk in image.chunks():
                    f.write(chunk)

            obj = Phone2.objects.create(
                name=request.data.get('name'),
                image=image_path
            )

            return Response({
                "id": obj.id
            }, status=status.HTTP_200_OK)


    def get(self, request):
        queryset = Phone2.objects.all()
        serializer = PhoneSerializer2(queryset, many=True, context={'request': request})
        return Response({
            'success': True,
            'phones': serializer.data
        }, status=status.HTTP_200_OK)


class GetImageView(APIView):
    def get(self, request):
        object = Phone2.objects.get(id=3)

        #########################################

        filename = object.image.name.split('/')[-1]
        response = HttpResponse(object.image, content_type='image/jpg')
        # response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response
