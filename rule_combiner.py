# rule_engine/rule_combiner.py
from typing import List
from .models import Node, NodeType, Operator

class RuleCombiner:
    def combine_rules(self, rules: List[Node]) -> Node:
        if not rules:
            raise ValueError("No rules to combine")
        if len(rules) == 1:
            return rules[0]
        
        # Combine rules with OR operator
        combined = rules[0]
        for rule in rules[1:]:
            combined = Node(
                type=NodeType.OPERATOR,
                operator=Operator.OR,
                left=combined,
                right=rule
            )
        
        return combined