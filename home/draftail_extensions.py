from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineStyleElementHandler,
)
from wagtail.admin.rich_text.editors.draftail.features import InlineStyleFeature


def register_inline_styling(
        features,
        feature_name,
        description,
        type_,
        tag='span',
        format=None,
        editor_style=None,
        label=None,
        icon=None
):
    control = {"type": type_, "description": description}
    if label:
        control["label"] = label
    elif icon:
        control["icon"] = icon
    else:
        control["label"] = description
    if editor_style:
        control["style"] = editor_style

    if not format:
        style_map = {"element": tag}
        markup_map = tag
    else:
        style_map = f'{tag} {format}'
        markup_map = f'{tag}[{format}]'

    features.register_editor_plugin(
        "draftail", feature_name, InlineStyleFeature(control)
    )
    db_conversion = {
        "from_database_format": {markup_map: InlineStyleElementHandler(type_)},
        "to_database_format": {"style_map": {type_: style_map}},
    }
    features.register_converter_rule("contentstate", feature_name, db_conversion)
