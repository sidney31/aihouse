from django.db import models
from django.forms.utils import ErrorList
from django.core.exceptions import ValidationError

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail import blocks

from home.blocks import (
    FunctionalDescBlock,
    CardCarouselBlock,
    TitleAndSubtitle,
)


class HomePage(Page):
    subHeader = StreamField([
        ("header", TitleAndSubtitle(label='Заголовок')),
        ("button", SnippetChooserBlock("home.ButtonSnippet",
                                       icon="th-list",
                                       template="home/tags/button.html")
         )
    ],
        block_counts={
            'header': {'min_num': 1, 'max_num': 1},
        },
        null=False,
        blank=False,
        default='',
        use_json_field=True)

    title_buttons = StreamField([
        ("button", SnippetChooserBlock("home.ButtonSnippet",
                                       icon="th-list",
                                       template="home/tags/button.html")
         )
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

    ##########################################################################

    content_panels = Page.content_panels + [
        FieldPanel('subHeader'),
        FieldPanel('title_buttons'),
        FieldPanel('functional_description'),
        FieldPanel('card_carousel'),
        FieldPanel('contacts'),
    ]


class BaseButtonSnippet(models.Model):
    bodyText = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.bodyText


@register_snippet
class ButtonSnippet(BaseButtonSnippet):
    height = models.IntegerField()
    width = models.IntegerField()
    bodyText = models.TextField(null=True, blank=True)
    url = models.URLField(blank=True, null=True)
    page = models.ForeignKey('wagtailcore.Page', blank=True, null=True, on_delete=models.SET_NULL)

    panels = [
        FieldPanel('height'),
        FieldPanel('width'),
        FieldPanel('bodyText'),
        MultiFieldPanel([
            FieldPanel('url'),
            PageChooserPanel('page')
        ],
            heading='RedirectTo'
        )
    ]

    class Meta:
        verbose_name = 'Кнопка'
        verbose_name_plural = 'Кнопки'

    def clean(self, *args, **kwargs):
        url = self.url
        page = self.page
        if page and url:
            message = "Кнопка может вести лишь на ОДИН ресурс"
            raise ValidationError(message=message)

        return super().clean()


@register_snippet
class TextLinkSnippet(BaseButtonSnippet):
    bodyText = models.TextField(null=True, blank=True)
    url = models.URLField()

    panels = [
        FieldPanel('bodyText'),
        FieldPanel('url'),
    ]

    class Meta:
        verbose_name = 'Текст-ссылка'
        verbose_name_plural = 'Текст-ссылки'
