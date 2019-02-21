import re

_PATTERN = re.compile(
    r'<'
    r'(?P<tag>\w*)'
    r'(?P<attributes>[\w\s="].*)?'
    r'/>'
)

_ATTRIBUTES_PATTERN = re.compile(
    r'(?P<key>\w+)'
    r'='
    r'"(?P<value>\w+)"'
)


def _parse_full_string(full_string):
    for single_string in _PATTERN.findall(full_string):
        yield _parse_single_tag_string(single_string)


def _parse_single_tag_string(single_string):
    tag, raw_attributes = single_string
    return {'tag': tag, 'attributes': _parse_attributes(raw_attributes)}


def _parse_attributes(raw_attributes):
    return dict(_ATTRIBUTES_PATTERN.findall(raw_attributes))


def parse(tags):
    return list(_parse_full_string(tags))
