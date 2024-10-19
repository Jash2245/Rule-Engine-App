# rule_engine/evaluator.py
from typing import Dict, Any
from .models import Node, NodeType, Operator

class RuleEvaluator:
    def evaluate_rule(self, node: Node, data: Dict[str, Any]) -> bool:
        if node.type == NodeType.OPERATOR:
            left_result = self.evaluate_rule(node.left, data)
            right_result = self.evaluate_rule(node.right, data)
            
            if node.operator == Operator.AND:
                return left_result and right_result
            elif node.operator == Operator.OR:
                return left_result or right_result
            
        elif node.type == NodeType.OPERAND:
            if node.field not in data:
                raise ValueError(f"Field {node.field} not found in data")
            
            field_value = data[node.field]
            
            if node.operator == Operator.GT:
                return field_value > node.value
            elif node.operator == Operator.LT:
                return field_value < node.value
            elif node.operator == Operator.EQ:
                return field_value == node.value
            elif node.operator == Operator.GTE:
                return field_value >= node.value
            elif node.operator == Operator.LTE:
                return field_value <= node.value
            
        return False