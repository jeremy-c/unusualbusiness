# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 16:38
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20160620_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.TextBlock(icon='italic', rows=3)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.TextBlock(required=True, rows=2, verbose_name='Pull quote')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(help_text='The name of the person or organization that the quote can be attributed to quote', required=False, verbose_name='Quote attribution to')), (b'link', wagtail.wagtailcore.blocks.URLBlock(help_text='Click quote to go to link.', required=False, verbose_name='Link'))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock()), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))]))]),
        ),
        migrations.AlterField(
            model_name='newsarticlepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.TextBlock(icon='italic', rows=3)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.TextBlock(required=True, rows=2, verbose_name='Pull quote')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(help_text='The name of the person or organization that the quote can be attributed to quote', required=False, verbose_name='Quote attribution to')), (b'link', wagtail.wagtailcore.blocks.URLBlock(help_text='Click quote to go to link.', required=False, verbose_name='Link'))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock()), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))]))], null=True),
        ),
        migrations.AlterField(
            model_name='newsarticlepage',
            name='body_nl',
            field=wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.TextBlock(icon='italic', rows=3)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.TextBlock(required=True, rows=2, verbose_name='Pull quote')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(help_text='The name of the person or organization that the quote can be attributed to quote', required=False, verbose_name='Quote attribution to')), (b'link', wagtail.wagtailcore.blocks.URLBlock(help_text='Click quote to go to link.', required=False, verbose_name='Link'))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock()), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))]))], null=True),
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.TextBlock(icon='italic', rows=3)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.TextBlock(required=True, rows=2, verbose_name='Pull quote')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(help_text='The name of the person or organization that the quote can be attributed to quote', required=False, verbose_name='Quote attribution to')), (b'link', wagtail.wagtailcore.blocks.URLBlock(help_text='Click quote to go to link.', required=False, verbose_name='Link'))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock()), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))]))]),
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.TextBlock(icon='italic', rows=3)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.TextBlock(required=True, rows=2, verbose_name='Pull quote')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(help_text='The name of the person or organization that the quote can be attributed to quote', required=False, verbose_name='Quote attribution to')), (b'link', wagtail.wagtailcore.blocks.URLBlock(help_text='Click quote to go to link.', required=False, verbose_name='Link'))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock()), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))]))], null=True),
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='body_nl',
            field=wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.TextBlock(icon='italic', rows=3)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.TextBlock(required=True, rows=2, verbose_name='Pull quote')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(help_text='The name of the person or organization that the quote can be attributed to quote', required=False, verbose_name='Quote attribution to')), (b'link', wagtail.wagtailcore.blocks.URLBlock(help_text='Click quote to go to link.', required=False, verbose_name='Link'))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock()), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))]))], null=True),
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.TextBlock(icon='italic', rows=3)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.TextBlock(required=True, rows=2, verbose_name='Pull quote')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(help_text='The name of the person or organization that the quote can be attributed to quote', required=False, verbose_name='Quote attribution to')), (b'link', wagtail.wagtailcore.blocks.URLBlock(help_text='Click quote to go to link.', required=False, verbose_name='Link'))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock()), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))]))]),
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.TextBlock(icon='italic', rows=3)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.TextBlock(required=True, rows=2, verbose_name='Pull quote')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(help_text='The name of the person or organization that the quote can be attributed to quote', required=False, verbose_name='Quote attribution to')), (b'link', wagtail.wagtailcore.blocks.URLBlock(help_text='Click quote to go to link.', required=False, verbose_name='Link'))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock()), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))]))], null=True),
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='body_nl',
            field=wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.TextBlock(icon='italic', rows=3)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.TextBlock(required=True, rows=2, verbose_name='Pull quote')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(help_text='The name of the person or organization that the quote can be attributed to quote', required=False, verbose_name='Quote attribution to')), (b'link', wagtail.wagtailcore.blocks.URLBlock(help_text='Click quote to go to link.', required=False, verbose_name='Link'))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock()), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))]))], null=True),
        ),
    ]
