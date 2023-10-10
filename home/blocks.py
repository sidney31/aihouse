from wagtail.blocks import CharBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock


class TitleButtonBlock(StructBlock):
    icon = CharBlock()
    title = CharBlock()

    class Meta:
        template = 'blocks/title_button_block.html'


class FunctionalDescBlock(StructBlock):
    header = CharBlock()
    description = CharBlock()

    class Meta:
        template = 'blocks/functional_desc_block.html'


class CardCarouselBlock(StructBlock):
    image = ImageChooserBlock()
    title = CharBlock()
    description = CharBlock()
    hint = CharBlock()

    class Meta:
        template = 'blocks/card_carousel_block.html'


class TitleAndSubtitle(StructBlock):
    title = CharBlock()
    subtitle = CharBlock()
