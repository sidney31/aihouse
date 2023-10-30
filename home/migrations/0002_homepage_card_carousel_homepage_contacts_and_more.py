# Generated by Django 4.2.6 on 2023-10-28 17:20

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='card_carousel',
            field=wagtail.fields.StreamField([('header', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('subtitle', wagtail.blocks.CharBlock())], label='Заголовок')), ('card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.CharBlock()), ('hint', wagtail.blocks.CharBlock())], label='Карточка'))], default='', use_json_field=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contacts',
            field=wagtail.fields.StreamField([], default='', use_json_field=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='functional_description',
            field=wagtail.fields.StreamField([('left_block', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.CharBlock())], label='Правый блок')), ('right_block', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.CharBlock())], label='Левый блок')), ('image', wagtail.images.blocks.ImageChooserBlock())], default='', use_json_field=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='subHeader',
            field=wagtail.fields.StreamField([('header', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('subtitle', wagtail.blocks.CharBlock())], label='Заголовок'))], default='', use_json_field=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_buttons',
            field=wagtail.fields.StreamField([('title_button', wagtail.blocks.StructBlock([('icon', wagtail.blocks.CharBlock()), ('title', wagtail.blocks.CharBlock())], label='Кнопка под верхним блоком'))], default='', use_json_field=True),
        ),
    ]
