from es_mapping.mapping_base import Mapping
from es_mapping.object_mapping import ObjectMapping
from .json_schema_type_parser import JsonSchemaTypeParser


class JsonSchemaObjectParser(JsonSchemaTypeParser):
    @property
    def schema_type(self) -> str:
        return "object"

    def parse_obj(self, obj, schema, mapping_builder: "JsonSchemaMappingBuilder") -> Mapping:
        return ObjectMapping(
            properties={
                key: mapping_builder.build_mapping(value, schema)
                for key, value in obj["properties"].items()
            }
        )