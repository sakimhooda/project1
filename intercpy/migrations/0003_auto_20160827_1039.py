# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intercpy', '0002_auto_20160826_0745'),
    ]

    operations = [
        migrations.CreateModel(
            name='internshipin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('internarea', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='internships',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('companyname', models.CharField(max_length=150)),
                ('postd', models.DateField()),
                ('lastd', models.DateField()),
                ('Estartd', models.DateField()),
                ('timeperiod', models.IntegerField()),
                ('abotcom', models.TextField()),
                ('abotintern', models.TextField()),
                ('internarea', models.ForeignKey(to='intercpy.internshipin')),
            ],
        ),
        migrations.CreateModel(
            name='internshiptype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interntype', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='internships',
            name='interntype',
            field=models.ForeignKey(to='intercpy.internshiptype'),
        ),
    ]
