import csv
from progressbar import ProgressBar

from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import Point

from ...models import Place

# Taken from the tech spec http://www.ordnancesurvey.co.uk/oswebsite/docs/technical-specifications/50k-gazetteer-technical-specification.pdf
FIELDNAMES = (
    "SEQ",         # Unique sequence number of the record.
    "KM_REF",      # The National Grid 1 km by 1 km square the feature or centre of the feature falls within on the 1:50 000 scale mapping.
    "DEF_NAM",     # Distinctive name of the feature the record describes
    "TILE_REF",    # The 1:50 000 Scale Colour Raster tile the feature or centre of the feature falls within.

    # The latitude and longitude degrees and minutes of the 1 km National Grid square the feature or centre of the feature falls within.
    "LAT_DEG", "LAT_MIN", "LONG_DEG", "LONG_MIN",

    # National Grid position of the centre point of the 1 km square the feature or centre of the feature falls within. 352500
    "NORTH", "EAST",

    "GMT",         # Greenwich Mean Time Position in relation to the Greenwich Meridian.
    "CO_CODE",     # Code representing the county or unitary authority boundary the definitive name falls within. See annexe B for a list.
    "COUNTY",      # Abbreviated county or unitary authority name.
    "FULL_COUNTY", # Full county or unitary authority name.
    "F_CODE",      # Describes what the feature is. See chapter 6 for complete list of definitions. 'T' represents town.
    "E_DATE",      # The date the record was last amended.
    "UPDATE_CO",   # Update code 'I' represents insert. 'A' represents amendment. 'D' represents deletion.
    "SHEET_1",     # Primary sheet no
    "SHEET_2",     # Second sheet no
    "SHEET_3",     # Third sheet no
)

class Command(BaseCommand):
    help = 'Load places from the OS 1:50k Gazetteer database'

    def handle(self, *args, **options):
        filename = args[0]
        reader = csv.DictReader(open(filename), fieldnames=FIELDNAMES, delimiter=':', quotechar='"')
        rownum = 0

        # hacky way to approximate the number of rows in the file
        pbar = ProgressBar( maxval=len(list(open(filename))) ).start()

        # There is nothing reliabe to use for detecting duplicates, delete database instead.
        Place.objects.filter(source=Place.SOURCE_OS_50K_GAZETEER).delete()

        for row in reader:
            rownum += 1
            pbar.update(rownum)

            name     = row['DEF_NAM']
            county = row['FULL_COUNTY']
            osgb36_x = int(row['EAST'])
            osgb36_y = int(row['NORTH'])

            # Skip blank lines, and roads which no name (like "A1")
            if not name:
                continue

            # create the name
            context_name = "{0}, {1}".format(name, county)

            # create a point for the centre
            centre = Point(osgb36_x, osgb36_y, srid=Place.SRID_OSGB36)
            centre.transform(Place.SRID_WGS84)

            # create the place
            place = Place(
                name = name,
                context_name = context_name,
                centre = centre,
                source = Place.SOURCE_OS_50K_GAZETEER,
            )

            # skip entries outside the allowed bonding boxes
            if not place.is_in_allowed_bounding_boxes():
                continue

            place.save()

        pbar.finish()
