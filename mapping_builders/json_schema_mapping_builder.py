import re
from typing import List

from mapping_builders import MappingBuilder
from es_mapping.mapping_base import Mapping
from mapping_builders.json_schema_parsers import JsonSchemaParser

REF_NORMALIZE_REGEX = re.compile("^#/")


def resolve_reference(reference, schema):
    normalized_ref = REF_NORMALIZE_REGEX.sub("", reference)
    path = normalized_ref.split("/")
    obj = schema
    for part in path:
        obj = obj[part]
    return obj


class JsonSchemaMappingBuilder(MappingBuilder):
    _parsers: List[JsonSchemaParser]

    def __init__(self):
        self._parsers = []

    def register_mapping_parser(self, parser: JsonSchemaParser):
        self._parsers.append(parser)

    def build_mapping(self, obj, schema) -> Mapping:
        # Handle references
        reference = obj.pop("$ref", None)
        if reference:
            obj.update(resolve_reference(reference, schema))

        for parser in self._parsers:
            if parser.can_parse(obj):
                return parser.parse_obj(obj, schema, self)
        raise Exception(f"No Parser found for object: {obj}")
