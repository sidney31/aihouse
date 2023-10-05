from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from .blocks import TitleButtonBlock


class HomePage(Page):
    big_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        default="Создавайте превосходные визуализации с легкостью",
    )

    small_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        default="Широкие возможности настройки | Простота в работе | Потрясающие 4K рендеры",
    )

    title_buttons = StreamField([
        ("title_button", TitleButtonBlock(
            features=[],
            label="Кнопка под верхним блоком",
        )),

    ],
        null=False,
        blank=False,
        default='',
        use_json_field=True)

    ###########################################################################

    content_panels = Page.content_panels + [
        FieldPanel('big_title'),
        FieldPanel('small_title'),
        FieldPanel('title_buttons'),
    ]
