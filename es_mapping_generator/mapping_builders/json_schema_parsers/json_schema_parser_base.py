from abc import ABCMeta, abstractmethod

from es_mapping_generator.es_mapping.mapping_base import Mapping


class JsonSchemaParser(metaclass=ABCMeta):
    @abstractmethod
    def parse_obj(self, obj, schema, mapping_builder: "JsonSchemaMappingBuilder") -> Mapping:
        raise NotImplementedError()

    @abstractmethod
    def can_parse(self, obj) -> bool:
        raise NotImplementedError()