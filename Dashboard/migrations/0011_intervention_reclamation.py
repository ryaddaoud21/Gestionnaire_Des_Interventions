# Generated by Django 3.2.14 on 2023-10-07 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0010_auto_20231005_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervention',
            name='reclamation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dashboard.reclamation'),
        ),
    ]