# Rule-Engine-App
## Overview:

This application serves as a rule engine for determining user eligibility based on various attributes. It leverages Abstract Syntax Trees (ASTs) to represent conditional rules, allowing for dynamic creation, combination, and modification of these rules.

### Key Features:

**AST-based rule representation:**

Rules are defined using ASTs for flexibility and extensibility.

**Dynamic rule creation and combination:**

Users can create and combine rules using the provided API.

**Rule evaluation:**

The application evaluates rules against user data to determine eligibility.

**Data storage:**

Rules and application metadata are stored in a database.

### Data Structure:

- Node: Represents a node in the AST.
- type: Indicates the node type (e.g., "operator", "operand").
- left: Reference to the left child node (for operators).
- right: Reference to the right child node (for operators).
- value: Optional value for operand nodes (e.g., number for comparisons).
  
### Data Storage:

- Database: Choose a suitable database (e.g., PostgreSQL, MySQL, MongoDB) to store rules and metadata.
#### Schema:
**Rules table:**
```
id (primary key)
rule_string (rule definition)
ast_json (JSON representation of the AST)
```
**Attributes table:**
```
id (primary key)
name (attribute name)
type (attribute type)
```
## Project Implementation

### First create your project folder "rule_engine_project" manually in Windows Explorer or use:
```bash
md rule_engine_project
cd rule_engine_project
```
- Open VS Code and select "File > Open Folder" (or Ctrl+K Ctrl+O) and select your "rule_engine_project" folder
- In VS Code, we'll create all files using the GUI:

- Click the "New Folder" icon in VS Code's explorer panel to create "rule_engine" folder
- Click the "New File" icon to create each file

### Here's the folder structure you need to create:
```
rule_engine_project/
    └── rule_engine/
        ├── __init__.py
        ├── models.py
        ├── parser.py
        ├── evaluator.py
        └── rule_combiner.py
    ├── main.py
    └── test_rules.py
```
### Create virtual environment through VS Code terminal (Ctrl + `):
```
python -m venv venv
venv\Scripts\activate
```
- Copy the code from the artifact into the respective files.
### Install required dependencies:
```
pip install pytest  # for testing
```
- To test the implementation, create a file test_rules.py:
### Run the tests:
```
pytest test_rules.py -v
```
- Install the required dependencies. Add this to a new file **requirements.txt**:
### Install these dependencies:
```bash
pip install -r requirements.txt
```
- Create a new file **app.py** for the FastAPI backend:
- Create a templates directory and add **index.html**:
- Create a **static directory** (it can be empty for now, but we'll use it if we need to add CSS or JavaScript files later).
### Run the application:
```bash
uvicorn app:app --reload
```
**Now you can access the application at http://localhost:8000. The interface allows you to:**

- Create new rules by providing:
```
Rule name
Rule string (e.g., age > 30 AND department = "Sales")
```

- Evaluate data against rules by:
```
Selecting a rule from the dropdown
Providing JSON data (e.g., {"age": 35, "department": "Sales"})
```

### Example usage:

- Create a rule:
```
Name: "sales_rule"
Rule: age > 30 AND department = "Sales"
```

- Evaluate data:
```
Select "sales_rule"
Data: {"age": 35, "department": "Sales"}
```


