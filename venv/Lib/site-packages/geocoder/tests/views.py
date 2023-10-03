from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.gis.geos import Point
from django.utils import simplejson as json

from ..models import Place

class GeocoderViewTests(TestCase):

    def setUp(self):

        self.lookup_url = reverse('geocoder-lookup')

        names = [
            'Bedford Place',
            'Bevan Avenue',
            'Bevan Close',
            'Bevan Way',
            'Chelsea',
        ]

        centre = Point(50, 2)

        for name in names:
            Place.objects.create(
                name = name,
                context_name = name + ", London",
                centre = centre,
                source = Place.SOURCE_OS_LOCATOR,
            )

    def get_lookup(self, term):
        resp = self.client.get(self.lookup_url, {"term": term})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp['Content-Type'], 'application/json')
        all = json.loads(resp.content)
        texts = [ x['text'] for x in all ]
        return { "all": all, "texts": texts }


    def test_no_matches(self):
        self.assertEqual( self.get_lookup('This should not match anything')['all'], [] )

    def test_one_matches(self):
        self.assertEqual( self.get_lookup('chelsea')['texts'], ['Chelsea, London'] )

    def test_many_matches(self):
        self.assertEqual(
            self.get_lookup('Bevan')['texts'],
            ['Bevan Avenue, London', 'Bevan Close, London', 'Bevan Way, London']
        )


