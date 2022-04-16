from es_mapping.keyword_mapping import KeywordMapping
from es_mapping.mapping_base import Mapping
from .json_schema_type_parser import JsonSchemaTypeParser


class JsonSchemaStringParser(JsonSchemaTypeParser):
    @property
    def schema_type(self) -> str:
        return "string"

    def parse_obj(self, obj, schema, mapping_builder: "JsonSchemaMappingBuilder") -> Mapping:
        return KeywordMapping()