from rule_engine.parser import RuleParser
from rule_engine.evaluator import RuleEvaluator
from rule_engine.rule_combiner import RuleCombiner

def main():
    # Create parser
    parser = RuleParser()
    
    # Sample rules
    rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
    
    # Parse rules into ASTs
    ast1 = parser.create_rule(rule1)
    ast2 = parser.create_rule(rule2)
    
    # Combine rules
    combiner = RuleCombiner()
    combined_ast = combiner.combine_rules([ast1, ast2])
    
    # Test evaluation
    evaluator = RuleEvaluator()
    test_data = {
        "age": 35,
        "department": "Sales",
        "salary": 60000,
        "experience": 3
    }
    
    result = evaluator.evaluate_rule(combined_ast, test_data)
    print(f"Evaluation result: {result}")

if __name__ == "__main__":
    main()