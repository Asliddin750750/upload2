from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from file.models import Phone
from file.serializers import PhoneSerializer


class AddPhoneView(APIView):
    def post(self, request):
        serializer = PhoneSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'success': False,
                'phone': serializer.errors
            }, status=status.HTTP_200_OK)
        serializer.save()
        return Response({
            'success': True,
            'phone': serializer.data
        }, status=status.HTTP_200_OK)

    def get(self, request):
        queryset = Phone.objects.all()
        serializer = PhoneSerializer(queryset, many=True, context={'request': request})
        return Response({
            'success': True,
            'phones': serializer.data
        }, status=status.HTTP_200_OK)
