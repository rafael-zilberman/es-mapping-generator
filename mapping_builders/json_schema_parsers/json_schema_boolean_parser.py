from es_mapping.boolean_mapping import BooleanMapping
from es_mapping.mapping_base import Mapping
from .json_schema_type_parser import JsonSchemaTypeParser


class JsonSchemaBooleanParser(JsonSchemaTypeParser):
    @property
    def schema_type(self) -> str:
        return "boolean"

    def parse_obj(self, obj, schema, mapping_builder: "JsonSchemaMappingBuilder") -> Mapping:
        return BooleanMapping()
