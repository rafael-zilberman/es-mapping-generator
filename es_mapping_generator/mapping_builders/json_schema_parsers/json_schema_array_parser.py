from es_mapping_generator.es_mapping.mapping_base import Mapping
from es_mapping_generator.es_mapping.nested_mapping import NestedMapping
from .json_schema_type_parser import JsonSchemaTypeParser


class JsonSchemaArrayParser(JsonSchemaTypeParser):
    @property
    def schema_type(self) -> str:
        return "array"

    def parse_obj(self, obj, schema, mapping_builder: "JsonSchemaMappingBuilder") -> Mapping:
        return NestedMapping(
            items=mapping_builder.build_mapping(obj["items"], schema)
        )