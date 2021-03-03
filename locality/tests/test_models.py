from django.http.response import Http404
from django.test import TestCase

from locality.models import Country, Territory


class TestCountry(TestCase):
    def setUp(self):
        self.country = Country.objects.create(iso2="mk", iso3="mkd", name="Macedonia")

    def test_repr(self):
        self.assertEqual(str(self.country), "Macedonia")

    def test_abbr(self):
        self.assertEqual(str(self.country.abbr), "mk")


class TestTerritory(TestCase):
    def setUp(self):
        self.country = Country.objects.create(iso2="mk", iso3="mkd", name="Macedonia")
        self.territory = Territory.objects.create(abbr="sk", name="skopje", country=self.country)

    def test_repr(self):
        self.assertEqual(str(self.territory), "skopje, Macedonia")


class TestCountryManager(TestCase):
    def setUp(self):
        self.country = Country.objects.create(iso2="mk", iso3="mkd", name="Macedonia")
        self.country1 = Country.objects.create(iso2="ca", iso3="can", name="Canada")

    def test_find_by_id(self):
        self.assertEqual(Country.objects.find(self.country.pk), self.country)

    def test_find_by_iso2(self):
        self.assertEqual(Country.objects.find("mk"), self.country)
        self.assertEqual(Country.objects.find("ca"), self.country1)

    def test_find_by_iso3(self):
        self.assertEqual(Country.objects.find("mkd"), self.country)
        self.assertEqual(Country.objects.find("can"), self.country1)

    def test_find_by_name(self):
        self.assertEqual(Country.objects.find("Macedonia"), self.country)
        self.assertEqual(Country.objects.find("Canada"), self.country1)

    def test_find_or_404(self):
        def will_raise():
            Country.objects.find_or_404("asda")

        self.assertRaises(Http404, will_raise)


class TestTerritoryManager(TestCase):
    def setUp(self):
        self.country = Country.objects.create(iso2="mk", iso3="mkd", name="Macedonia")
        self.country1 = Country.objects.create(iso2="ca", iso3="can", name="Canada")
        self.territory1 = Territory.objects.create(abbr="t1", name="Turf1", country=self.country)
        self.territory2 = Territory.objects.create(abbr="t2", name="Turf2", country=self.country)
        self.territory3 = Territory.objects.create(abbr="t3", name="Turf3", country=self.country1)
        self.territory4 = Territory.objects.create(abbr="t4", name="Turf4", country=self.country1)
