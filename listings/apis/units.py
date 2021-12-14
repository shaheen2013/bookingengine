import moment
from django.db.models import Q
from rest_framework import generics

from listings.models import Listing
from listings.serializers.unit_serializer import UnitSerializer


class UnitView(generics.ListAPIView):
    serializer_class = UnitSerializer

    def get_queryset(self):
        """
        listing without blocked days in the range and below max_price
        :return QuerySet:
        """
        # query param
        max_price = self.request.GET.get('max_price')
        check_in = self.request.GET.get('check_in')
        check_out = self.request.GET.get('check_out')
        # get listing queryset
        queryset = Listing.objects.filter()
        if max_price:
            # filter data for max price
            queryset.filter(booking_info__price__lte=max_price)
        if check_in and check_out:
            # get date list between check in and check out
            dates = list(self.dates_bwn_twodates(moment.date(check_in), moment.date(check_out)))  # dates as a list
            # filter data for check in check out date
            queryset.filter(~Q(booked_listing__check_in__in=dates) | ~Q(booked_listing__check_out__in=dates))
        return queryset.all()

    def dates_bwn_twodates(self, check_in, check_out):
        """
        date list between check_in and check_out
        :param check_in:
        :param check_out:
        """
        diff = abs(check_in.diff(check_out).days)

        for n in range(0, diff + 1):
            yield check_in.strftime("%Y-%m-%d")
            check_in = (check_in).add(days=1)
