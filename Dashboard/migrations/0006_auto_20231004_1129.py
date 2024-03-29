# Generated by Django 3.2.14 on 2023-10-04 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0005_reclamation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamation',
            name='intervention',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dashboard.intervention'),
        ),
        migrations.AddField(
            model_name='reclamation',
            name='intervention_cree',
            field=models.BooleanField(default=False),
        ),
    ]
