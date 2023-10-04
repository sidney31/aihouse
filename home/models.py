from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from .blocks import FigCaptionBlock

class HomePage(Page):
    subtitle = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    rtrbody = RichTextField(
        blank=True,
        null=True
    )

    bg_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    body = StreamField([
        ('figcaptionblock', FigCaptionBlock()),
        ('rtfblock', blocks.RichTextBlock(label='Текст', 
                                          help_text='Описание',
                                          features={'h1', 'bold', 'link', 'code'})),
        ('image', ImageChooserBlock(label='Фото', 
                                    help_text='Изображение',
                                    template='blocks/imgblock.html')),
        ('youtubeblock', EmbedBlock(label='Видео', 
                                    help_text='Ютуб',
                                    icon='success')),
    ],
    block_counts={
        'rtfblock': {'min_num': 1},
        'image': {'max_num': 3},
    },
    use_json_field=True,
    blank=True)

###########################################################################

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('rtrbody'),
        FieldPanel('bg_image'),
        FieldPanel('body'),
    ]