from textwrap import dedent

from django.test import Client, TestCase
from django.urls import reverse


class TestCountriesView(TestCase):

    fixtures = ["locality.json"]

    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)

    def test_get_no_attrs(self):
        path = reverse("locality-countries")
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"""{"iso2": "ZW", "iso3": "ZWE", "name": "Zimbabwe"}""", response.content)

    def test_get_json(self):
        path = reverse("locality-countries", kwargs={"format": "json"})
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"""{"iso2": "ZW", "iso3": "ZWE", "name": "Zimbabwe"}""", response.content)

    def test_get_xml(self):
        path = reverse("locality-countries", kwargs={"format": "xml"})
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"""{"iso2": "ZW", "iso3": "ZWE", "name": "Zimbabwe"}""", response.content)
        needle = (
            dedent(
                """
            <object model="locality.country" pk="894"><field name="iso2" type="CharField">ZM</field>
            <field name="iso3" type="CharField">ZMB</field><field name="name" type="CharField">Zambia</field>
            </object><object model="locality.country" pk="716"><field name="iso2" type="CharField">ZW</field>
            <field name="iso3" type="CharField">ZWE</field><field name="name" type="CharField">Zimbabwe</field>
            </object>
            """
            )
            .replace("\n", "")
            .encode("utf-8")
        )
        self.assertIn(
            needle,
            response.content,
        )

    def test_get_find(self):
        path = reverse("locality-countries-find", kwargs={"country": "mk"})
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"""{"iso2": "ZW", "iso3": "ZWE", "name": "Zimbabwe"}""", response.content)
        self.assertIn(b"""{"iso2": "MK", "iso3": "MKD", "name": "Macedonia"}""", response.content)


class TestTerritoriesView(TestCase):

    fixtures = ["locality.json"]

    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)

    def test_get_no_attrs(self):
        path = reverse("locality-territories")
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"""{"abbr": "ZH", "name": "Zuid-Holland",""", response.content)

    def test_get_json(self):
        path = reverse("locality-territories", kwargs={"format": "json"})
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"""{"abbr": "ZH", "name": "Zuid-Holland",""", response.content)

    def test_get_xml(self):
        path = reverse("locality-territories", kwargs={"format": "xml"})
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"""{"abbr": "ZH", "name": "Zuid-Holland",""", response.content)
        self.assertIn(
            b"""<field name="abbr" type="CharField">ZH</field><field name="name" type="CharField">Zurich</field>""",
            response.content,
        )

    def test_get_find_by_country(self):
        path = reverse("locality-territories-by-country", kwargs={"country": "us"})
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"""{"abbr": "ZH", "name": "Zuid-Holland",""", response.content)
        self.assertIn(b"""{"abbr": "WV", "name": "West Virginia", """, response.content)
