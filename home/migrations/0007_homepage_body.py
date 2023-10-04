# Generated by Django 4.2.5 on 2023-10-04 12:33

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_bg_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('rtfblock', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('youtubeblock', wagtail.embeds.blocks.EmbedBlock())], blank=True, use_json_field=True),
        ),
    ]
