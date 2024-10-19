# test_rules.py
import pytest
from rule_engine.parser import RuleParser
from rule_engine.evaluator import RuleEvaluator
from rule_engine.rule_combiner import RuleCombiner
from rule_engine.models import NodeType, Operator

def test_simple_comparison():
    parser = RuleParser()
    rule = 'age > 30'
    ast = parser.create_rule(rule)
    assert ast is not None
    assert ast.type == NodeType.OPERAND
    assert ast.operator == Operator.GT
    assert ast.field == "age"
    assert ast.value == 30

def test_and_operation():
    parser = RuleParser()
    rule = '(age > 30 AND department = "Sales")'
    ast = parser.create_rule(rule)
    assert ast is not None
    assert ast.type == NodeType.OPERATOR
    assert ast.operator == Operator.AND
    
    # Check left child (age > 30)
    assert ast.left.type == NodeType.OPERAND
    assert ast.left.field == "age"
    assert ast.left.operator == Operator.GT
    assert ast.left.value == 30
    
    # Check right child (department = "Sales")
    assert ast.right.type == NodeType.OPERAND
    assert ast.right.field == "department"
    assert ast.right.operator == Operator.EQ
    assert ast.right.value == "Sales"

def test_rule_evaluation():
    parser = RuleParser()
    evaluator = RuleEvaluator()
    
    rule = '(age > 30 AND department = "Sales")'
    ast = parser.create_rule(rule)
    
    # Should return True
    data1 = {"age": 35, "department": "Sales"}
    assert evaluator.evaluate_rule(ast, data1) == True
    
    # Should return False
    data2 = {"age": 25, "department": "Sales"}
    assert evaluator.evaluate_rule(ast, data2) == False

def test_rule_combination():
    parser = RuleParser()
    combiner = RuleCombiner()
    evaluator = RuleEvaluator()
    
    rule1 = '(age > 30 AND department = "Sales")'
    rule2 = '(age < 25 AND department = "Marketing")'
    
    ast1 = parser.create_rule(rule1)
    ast2 = parser.create_rule(rule2)
    
    combined = combiner.combine_rules([ast1, ast2])
    assert combined is not None
    assert combined.type == NodeType.OPERATOR
    assert combined.operator == Operator.OR
    
    # Test combined rules
    data = {"age": 35, "department": "Sales"}
    assert evaluator.evaluate_rule(combined, data) == True

def test_invalid_rule():
    parser = RuleParser()
    with pytest.raises(ValueError):
        parser.create_rule("age > ")  # Incomplete rule

def test_missing_field():
    parser = RuleParser()
    evaluator = RuleEvaluator()
    
    rule = "age > 30"
    ast = parser.create_rule(rule)
    
    data = {"department": "Sales"}  # Missing age field
    with pytest.raises(ValueError):
        evaluator.evaluate_rule(ast, data)