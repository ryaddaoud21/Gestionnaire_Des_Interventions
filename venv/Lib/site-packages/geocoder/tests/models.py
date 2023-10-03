from django.test import TestCase
from django.test.utils import override_settings

from ..models import Place

from django.contrib.gis.geos import Point


class GeocoderModelTests(TestCase):

    @override_settings(GEOCODER_BOUNDING_BOXES=(
        # xmin, ymin, xmax, ymax
        ( -1,   50,   1,    52 ),
    ))
    def test_is_in_allowed_bounding_boxes(self):
        defaults = dict(context_name="Context", source=Place.SOURCE_OS_LOCATOR)
        good_place = Place(name='Allowed', centre=Point(0, 51),  **defaults)
        bad_place  = Place(name='Bad',     centre=Point(-2, 51), **defaults)

        self.assertTrue(good_place.is_in_allowed_bounding_boxes())
        self.assertFalse(bad_place.is_in_allowed_bounding_boxes())
