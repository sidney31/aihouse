from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin

from .blocks import TitleButtonBlock, FunctionalDescBlock, Column, CardCarouselBlock, TitleAndSubtitle
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks


class HomePage(RoutablePageMixin, Page):
    subHeader = StreamField([
        ("header", TitleAndSubtitle(
            label='Заголовок'
        )),
    ],
        block_counts={
            'header': {'min_num': 1, 'max_num': 1},
        },
        null=False,
        blank=False,
        default='',
        use_json_field=True)

    title_buttons = StreamField([
        ("title_button", TitleButtonBlock(
            label="Кнопка под верхним блоком",
        )),

    ],
        null=False,
        blank=False,
        default='',
        use_json_field=True)

    functional_description = StreamField([
        ("left_block", FunctionalDescBlock(
            label="Правый блок",
        )),
        ("right_block", FunctionalDescBlock(
            label="Левый блок",
        )),
        ('image', ImageChooserBlock()),
    ],
        block_counts={
            'left_block': {'min_num': 2},
            'right_block': {'min_num': 2},
            'image': {'mix_num': 1, 'max_num': 1},
        },

        null=False,
        blank=False,
        default='',
        use_json_field=True)

    card_carousel = StreamField([
        ("header", TitleAndSubtitle(
            label='Заголовок'
        )),
        ("card", CardCarouselBlock(
            label='Карточка'
        )),
    ],
        null=False,
        blank=False,
        default='',
        use_json_field=True)

    contacts = StreamField([
        ("column", blocks.RichTextBlock(
            label='Столбец'
        )),
    ],
        block_counts={
            'column': {'mix_num': 3, 'max_num': 3},
        },

        null=False,
        blank=False,
        default='',
        use_json_field=True)

    ###########################################################################

    content_panels = Page.content_panels + [
        FieldPanel('subHeader'),
        FieldPanel('title_buttons'),
        FieldPanel('functional_description'),
        FieldPanel('card_carousel'),
        FieldPanel('contacts'),
    ]