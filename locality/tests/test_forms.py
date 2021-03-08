from django.core.exceptions import ValidationError
from django.test import TestCase

from locality.forms import CountrySelectField, CountrySelectWidget
from locality.models import Country


class TestCountrySelectField(TestCase):
    def setUp(self):
        self.country = Country.objects.create(iso2="mk", iso3="mkd", name="Macedonia")

    def test_country_select_field_clean(self):
        f = CountrySelectField()
        cleaned = f.clean("mk")
        self.assertEqual(cleaned, self.country)

    def test_country_select_field_clean_empty(self):
        f = CountrySelectField(required=False)
        cleaned = f.clean("")
        self.assertEqual(cleaned, "")

    def test_country_select_field_clean_missing(self):
        f = CountrySelectField()

        def clean():
            return f.clean("mkdd")

        self.assertRaises(ValidationError, clean)


class TestCountrySelectWidget(TestCase):
    def setUp(self):
        self.country = Country.objects.create(iso2="mk", iso3="mkd", name="Macedonia")
        Country.objects.create(iso2="ca", iso3="can", name="Canada")
        self.widget = CountrySelectWidget()

    def test_widget_choices(self):
        self.assertEqual(self.widget.choices, [("ca", "Canada"), ("mk", "Macedonia")])

    def test_widget_render_is_select(self):
        rendered = self.widget.render("name", "")
        self.assertIn('<select name="name">', rendered)
