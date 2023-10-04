from wagtail.blocks import CharBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock

class FigCaptionBlock(StructBlock):
    figure = ImageChooserBlock()
    caption = CharBlock()

    class Meta:
        icon = 'image'
        template = 'blocks/fig_caption_block.html'