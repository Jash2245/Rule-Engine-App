from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import json
from rule_engine import RuleParser, RuleEvaluator, RuleCombiner

app = FastAPI()

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Store rules in memory (in a real application, you'd use a database)
rules_store = {}
rule_parser = RuleParser()
rule_evaluator = RuleEvaluator()
rule_combiner = RuleCombiner()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "rules": rules_store}
    )

@app.post("/create_rule")
async def create_rule(rule_name: str = Form(...), rule_string: str = Form(...)):
    try:
        # Parse and store the rule
        ast = rule_parser.create_rule(rule_string)
        rules_store[rule_name] = {
            "string": rule_string,
            "ast": ast
        }
        return {"status": "success", "message": "Rule created successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/evaluate_data")
async def evaluate_data(rule_name: str = Form(...), data: str = Form(...)):
    try:
        # Get the rule
        rule = rules_store.get(rule_name)
        if not rule:
            return {"status": "error", "message": "Rule not found"}
        
        # Parse the JSON data
        json_data = json.loads(data)
        
        # Evaluate the rule
        result = rule_evaluator.evaluate_rule(rule["ast"], json_data)
        
        return {
            "status": "success", 
            "result": result,
            "message": "Evaluation successful"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/rules")
async def get_rules():
    return {
        "rules": [
            {"name": name, "string": rule["string"]} 
            for name, rule in rules_store.items()
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)