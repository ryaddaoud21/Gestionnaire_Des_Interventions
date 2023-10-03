# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Place', fields ['name']
        db.create_index('geocoder_place', ['name'])


    def backwards(self, orm):
        # Removing index on 'Place', fields ['name']
        db.delete_index('geocoder_place', ['name'])


    models = {
        'geocoder.place': {
            'Meta': {'object_name': 'Place'},
            'centre': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'context_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_index': 'True'}),
            'source': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['geocoder']