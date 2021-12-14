from rest_framework import serializers

from listings.models import Listing, BookingInfo


class BookingInfoRelatedField(serializers.RelatedField):

    def to_representation(self, value: BookingInfo):
        return value.price


class UnitSerializer(serializers.ModelSerializer):
    price = BookingInfoRelatedField(many=False, read_only=True, source='booking_info')
    listing_type = serializers.SerializerMethodField('get_listing_type')

    def get_listing_type(self, obj: Listing):
        """
        listing_type display name
        :param obj:
        :return:
        """
        return obj.get_listing_type_display()

    class Meta:
        model = Listing
        fields = ('listing_type', 'title', 'country', 'city', 'price',)
