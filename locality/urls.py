from django.contrib import admin
from django.urls import re_path

from .views import countries, territories


admin.autodiscover()

urlpatterns = [
    re_path(r"^(?P<to>(?:json|xml|yaml))/countries/(?:all/?)?$", countries, name="locality-countries"),
    re_path(r"^(?P<to>(?:json|xml|yaml))/territories/(?:all/?)?$", territories, name="locality-territories"),
    re_path(
        r"^(?P<to>(?:json|xml|yaml))/territories(?:/(?P<country>(?:\d+|\w{2}|\w{3}))/?)?$",
        territories,
        name="locality-territories-by-country",
    ),
    re_path(
        r"^(?P<to>(?:json|xml|yaml))/country/(?P<country>(?:\d+|\w{2}|\w{3}))/?$",
        countries,
        name="locality-countries-find",
    ),
]
