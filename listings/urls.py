from django.urls import path

from listings.apis.units import UnitView

urlpatterns = [
    path('api/v1/units/', UnitView.as_view(), name="units"),
]
