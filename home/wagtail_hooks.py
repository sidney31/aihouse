from wagtail import hooks
from .draftail_extensions import *
from .icons_svg import *


@hooks.register("register_rich_text_features")
def register_larger_styling(features):
    register_inline_styling(
        features=features,
        feature_name='larger',
        type_='LARGER',
        tag='span',
        format='style="font-size:larger;"',
        editor_style={'font-size': 'larger'},
        description='Increase Font',
        icon=DRAFTAIL_ICONS.increase_font
    )


@hooks.register("register_rich_text_features")
def register_smaller_styling(features):
    register_inline_styling(
        features=features,
        feature_name='smaller',
        type_='SMALLER',
        tag='span',
        format='style="font-size:smaller;"',
        editor_style={'font-size': 'smaller'},
        description='Decrease Font',
        icon=DRAFTAIL_ICONS.decrease_font
    )
