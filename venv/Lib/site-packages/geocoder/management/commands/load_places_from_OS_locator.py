import csv
from progressbar import ProgressBar

from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import Point

from ...models import Place


# Taken from the tech spec http://www.ordnancesurvey.co.uk/oswebsite/docs/user-guides/os-locator-user-guide.pdf
FIELDNAMES = (
    "Name", # Feature name
    "Classification", # Road Number Classification
    "Centx", # X coord for Centre point of road object
    "Centy", # Y coord for Centre point of road object
    "Minx",  # X coord for SW corner of the road object box
    "Maxx",  # X cord for NE corner of road object box
    "Miny",  # Y coord for SW corner of the road object box
    "Maxy",  # Y coord for NE corner of road object box
    "Settlement", # Town in which the centre of the object falls
    "Locality", # Dataset with a description for the point at the centre of the object
    "Cou_Unit", # County or Unitary Authority in which the centre of the object falls, according to the latest Boundary-Line dataset
    "Local Authority", # Local Authority in which the centre of the object falls, according to the latest Boundary-Line dataset
    "Tile_10k", # 1:10 000 scale tile reference for the centre point of the object
    "Tile_25k", # 1:25 000 scale tile reference for the centre point of the object
    "Source", # Source of information
)

class Command(BaseCommand):
    help = 'Load places from the OS Locator database'

    def handle(self, *args, **options):
        filename = args[0]
        reader = csv.DictReader(open(filename), fieldnames=FIELDNAMES, delimiter=':', quotechar='"')
        rownum = 0

        # hacky way to approximate the number of rows in the file
        pbar = ProgressBar( maxval=len(list(open(filename))) ).start()

        # There is nothing reliabe to use for detecting duplicates, delete database instead.
        Place.objects.filter(source=Place.SOURCE_OS_LOCATOR).delete()

        for row in reader:
            rownum += 1
            pbar.update(rownum)

            name     = row['Name']
            locality = row['Locality']
            osgb36_x = int(row['Centx'])
            osgb36_y = int(row['Centy'])

            # Skip blank lines, and roads which no name (like "A1")
            if not name:
                continue

            # create the name
            context_name = "{0}, {1}".format(name, locality)

            # create a point for the centre
            centre = Point(osgb36_x, osgb36_y, srid=Place.SRID_OSGB36)
            centre.transform(Place.SRID_WGS84)

            # create the place
            place = Place(
                name = name,
                context_name = context_name,
                centre = centre,
                source = Place.SOURCE_OS_LOCATOR,
            )

            # skip entries outside the allowed bonding boxes
            if not place.is_in_allowed_bounding_boxes():
                continue

            place.save()

        pbar.finish()

