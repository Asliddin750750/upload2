from rest_framework import serializers

from file.models import Phone


class PhoneSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Phone
        fields = '__all__'

    # def get_image(self, obj):
    #     try:
    #         request = self.context.get('request')
    #         image_url = obj.image.url
    #         return request.build_absolute_uri(image_url)
    #     except:
    #         return obj



