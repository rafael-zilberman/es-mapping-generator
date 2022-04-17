from es_mapping_generator.es_mapping.keyword_mapping import KeywordMapping
from es_mapping_generator.es_mapping.mapping_base import Mapping
from .json_schema_parser_base import JsonSchemaParser


class JsonSchemaEnumParser(JsonSchemaParser):
    def can_parse(self, obj) -> bool:
        return "enum" in obj

    def parse_obj(self, obj, schema, mapping_builder: "JsonSchemaMappingBuilder") -> Mapping:
        return KeywordMapping()