from typing import Dict

from .mapping_base import Mapping


class ObjectMapping(Mapping):
    type: str = "object"
    properties: Dict[str, Mapping] = {}