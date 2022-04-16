from abc import ABCMeta, abstractmethod

from .json_schema_parser_base import JsonSchemaParser


class JsonSchemaTypeParser(JsonSchemaParser, metaclass=ABCMeta):
    @property
    @abstractmethod
    def schema_type(self) -> str:
        raise NotImplementedError()

    def can_parse(self, obj) -> bool:
        return obj.get("type") == self.schema_type