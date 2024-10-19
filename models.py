from dataclasses import dataclass
from typing import Optional, Union, Dict, Any
from enum import Enum

class NodeType(Enum):
    OPERATOR = "operator"
    OPERAND = "operand"

class Operator(Enum):
    AND = "AND"
    OR = "OR"
    GT = ">"
    LT = "<"
    EQ = "="
    GTE = ">="
    LTE = "<="

@dataclass
class Node:
    type: NodeType
    left: Optional['Node'] = None
    right: Optional['Node'] = None
    value: Optional[Any] = None
    operator: Optional[Operator] = None
    field: Optional[str] = None