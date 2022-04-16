from .mapping_base import Mapping


class NestedMapping(Mapping):
    type: str = "nested"
    items: Mapping