from wagtail.blocks import CharBlock, StructBlock


class TitleButtonBlock(StructBlock):
    icon = CharBlock()
    title = CharBlock()

    class Meta:
        icon = 'image'
        template = 'blocks/title_button_block.html'
