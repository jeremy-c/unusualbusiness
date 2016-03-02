# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_organizationpage_tags'),
        ('howtos', '0002_howtopage_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowToPageOrganizationPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('how_to_page', modelcluster.fields.ParentalKey(related_name='organization_pages', to='howtos.HowToPage')),
                ('organization', models.ForeignKey(related_name='how_to_page', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='organizations.OrganizationPage', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
