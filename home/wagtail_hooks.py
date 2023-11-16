from wagtail import hooks

from .draftail_extensions import *

@hooks.register("register_rich_text_features")
def register_col_sm_styling(features):
    register_inline_styling(
        features=features,
        feature_name='small',
        type_='SMALL',
        tag='span',
        format='style="col-sm-4"',
        editor_style={'col-sm-4'},
        description='Small column size',
        label='small',
    )


@hooks.register("register_rich_text_features")
def register_col_md_styling(features):
    register_inline_styling(
        features=features,
        feature_name='medium',
        type_='MEDIUM',
        tag='span',
        format='style="col-sm-2"',
        editor_style={'col-sm-2'},
        description='Medium column size',
        label='medium',
    )


@hooks.register("register_rich_text_features")
def register_col_lg_styling(features):
    register_inline_styling(
        features=features,
        feature_name='large',
        type_='LARGER',
        tag='span',
        format='style="col"',
        editor_style={'col'},
        description='Large column size',
        label='large',
    )
