# Generated by Django 3.0.7 on 2020-06-14 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0007_auto_20200614_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='explores',
            old_name='distance_from_bang',
            new_name='dist_from_bang',
        ),
    ]
