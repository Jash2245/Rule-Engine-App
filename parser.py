# rule_engine/parser.py
from typing import List
from .models import Node, NodeType, Operator

class RuleParser:
    def __init__(self):
        self.tokens = []
        self.current = 0
    
    def tokenize(self, rule_string: str) -> List[str]:
        # Replace operators with space-padded versions for easier splitting
        rule_string = rule_string.replace('(', ' ( ')
        rule_string = rule_string.replace(')', ' ) ')
        rule_string = rule_string.replace('>=', ' >= ')
        rule_string = rule_string.replace('<=', ' <= ')
        rule_string = rule_string.replace('>', ' > ')
        rule_string = rule_string.replace('<', ' < ')
        rule_string = rule_string.replace('=', ' = ')
        
        # Split into tokens and filter out empty strings
        return [token.strip() for token in rule_string.split() if token.strip()]

    def peek(self) -> str:
        if self.current < len(self.tokens):
            return self.tokens[self.current]
        return ""

    def create_rule(self, rule_string: str) -> Node:
        self.tokens = self.tokenize(rule_string)
        self.current = 0
        return self.parse_expression()
    
    def parse_expression(self) -> Node:
        if '(' in self.tokens:
            return self.parse_group()
        else:
            return self.parse_comparison()

    def parse_group(self) -> Node:
        if self.peek() != '(':
            return self.parse_comparison()
            
        self.current += 1  # Skip '('
        left = self.parse_expression()
        
        if self.current >= len(self.tokens):
            raise ValueError("Missing operator after left expression")
            
        op_token = self.tokens[self.current]
        if op_token not in ('AND', 'OR'):
            raise ValueError(f"Invalid operator: {op_token}")
            
        self.current += 1
        right = self.parse_expression()
        
        if self.current >= len(self.tokens) or self.tokens[self.current] != ')':
            raise ValueError("Missing closing parenthesis")
            
        self.current += 1
        
        return Node(
            type=NodeType.OPERATOR,
            operator=Operator[op_token],
            left=left,
            right=right
        )
    
    def parse_comparison(self) -> Node:
        if self.current >= len(self.tokens):
            raise ValueError("Unexpected end of expression")
            
        field = self.tokens[self.current]
        self.current += 1
        
        if self.current >= len(self.tokens):
            raise ValueError("Missing operator")
            
        op_token = self.tokens[self.current]
        if op_token not in ('>', '<', '=', '>=', '<='):
            raise ValueError(f"Invalid comparison operator: {op_token}")
            
        self.current += 1
        
        if self.current >= len(self.tokens):
            raise ValueError("Missing value")
            
        value = self.tokens[self.current]
        self.current += 1
        
        # Strip quotes from string values
        if (value.startswith('"') and value.endswith('"')) or \
           (value.startswith("'") and value.endswith("'")):
            value = value[1:-1]
        # Convert numeric values
        elif value.isdigit():
            value = int(value)
        elif value.replace('.', '').isdigit():
            value = float(value)
            
        return Node(
            type=NodeType.OPERAND,
            field=field,
            operator=Operator(op_token),
            value=value
        )