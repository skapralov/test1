from rest_framework import serializers

from test1.apps.app.models import Request, Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
        read_only_fields = ('uuid', 'created')


class RequestSerializer(serializers.ModelSerializer):
    offers = OfferSerializer(many=True, read_only=True)

    class Meta:
        model = Request
        fields = '__all__'
        read_only_fields = ('uuid', 'created')
