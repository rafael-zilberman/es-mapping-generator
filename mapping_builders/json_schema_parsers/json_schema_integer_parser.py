from es_mapping.integer_mapping import IntegerMapping
from es_mapping.mapping_base import Mapping
from . import JsonSchemaParser
from .json_schema_type_parser import JsonSchemaTypeParser


class JsonSchemaIntegerParser(JsonSchemaParser):
    def can_parse(self, obj) -> bool:
        return obj.get("type") in ["integer", "number"]

    def parse_obj(self, obj, schema, mapping_builder: "JsonSchemaMappingBuilder") -> Mapping:
        return IntegerMapping()
