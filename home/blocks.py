from wagtail.blocks import CharBlock, StructBlock


class TitleButtonBlock(StructBlock):
    icon = CharBlock()
    title = CharBlock()

    class Meta:
        icon = 'image'
        template = 'blocks/title_button_block.html'


class FunctionalDescBlock(StructBlock):
    header = CharBlock()
    description = CharBlock()

    class Meta:
        icon = 'image'
        template = 'blocks/functional_desc_block.html'
