from abc import ABCMeta, abstractmethod

from es_mapping.mapping_base import Mapping


class MappingBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_mapping(self, obj, schema) -> Mapping:
        raise NotImplementedError()
