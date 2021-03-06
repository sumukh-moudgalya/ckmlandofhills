# Generated by Django 3.0.7 on 2020-06-21 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0020_homestays_premium'),
    ]

    operations = [
        migrations.CreateModel(
            name='MalnadSpecials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('rank', models.PositiveIntegerField()),
                ('desc', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('google_map_link', models.TextField()),
                ('google_map_html', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='homestays',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='homestays'),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='hotels'),
        ),
    ]
