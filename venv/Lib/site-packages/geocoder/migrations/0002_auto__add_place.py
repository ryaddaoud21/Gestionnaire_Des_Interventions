# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table('geocoder_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('context_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('centre', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('source', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('geocoder', ['Place'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table('geocoder_place')


    models = {
        'geocoder.place': {
            'Meta': {'object_name': 'Place'},
            'centre': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'context_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'source': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['geocoder']