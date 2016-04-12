# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0025_auto_20160412_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportarticlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(classname='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(classname='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())]))]),
        ),
        migrations.AlterField(
            model_name='reportarticlepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(classname='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(classname='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())]))], null=True),
        ),
        migrations.AlterField(
            model_name='reportarticlepage',
            name='body_nl',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(classname='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(classname='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())]))], null=True),
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(classname='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(classname='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())]))]),
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(classname='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(classname='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())]))], null=True),
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='body_nl',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(classname='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(classname='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())]))], null=True),
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(classname='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(classname='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())]))]),
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(classname='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(classname='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())]))], null=True),
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='body_nl',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(classname='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(classname='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())]))], null=True),
        ),
    ]
