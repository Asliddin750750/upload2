from rest_framework import serializers

from upload.models import Car


class CarSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    class Meta:
        model = Car
        fields = ('brand', 'photo')

    def get_photo(self, obj):
        try:
            request = self.context.get('request')
            photo_url = obj.dirname + obj.name
            print(photo_url)
            return request.build_absolute_uri(photo_url)
        except:
            pass
