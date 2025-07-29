import json
import os
import sys
import random
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuration
filename = "data.json"
port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000

# Input field validation schema
input_fields = [
    {"key": "name", "type": "str"},
    {"key": "size", "type": "int"},
    {"key": "readOnly", "type": "bool"}
]

# Global tables list
tables = []

def read_from_disk():
    """Read tables data from disk if file exists"""
    global tables
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            tables = json.load(f)

def write_to_disk():
    """Write tables data to disk"""
    with open(filename, 'w') as f:
        json.dump(tables, f)

def error_response(status_code, message):
    """Return error response with given status code and message"""
    print(f"Error: {message}")
    return jsonify({"message": message}), status_code

def validate_field_type(value, expected_type):
    """Validate if value matches expected type"""
    if expected_type == "str":
        return isinstance(value, str)
    elif expected_type == "int":
        return isinstance(value, int)
    elif expected_type == "bool":
        return isinstance(value, bool)
    return False

@app.route('/table', methods=['POST'])
def create_table():
    """
    Create a table resource. The JSON body should be:
    {
        name: string
        size: number
        readOnly: boolean
    }
    
    The response will be the created resource, including a string ID field.
    """
    table = request.get_json()
    print(f"POST /table {table}")
    
    # Validate inputs
    for field in input_fields:
        if field["key"] not in table:
            return error_response(400, f"Missing attribute: {field['key']}")
        
        if not validate_field_type(table[field["key"]], field["type"]):
            actual_type = type(table[field["key"]]).__name__
            return error_response(400, f"Field {field['key']} should be type {field['type']}, received type {actual_type}")
    
    # Add metadata
    table["id"] = str(random.randint(0, 999999))
    table["createdAt"] = datetime.now().isoformat()
    table["modifiedAt"] = table["createdAt"]
    
    tables.append(table)
    write_to_disk()
    print(f"Added table: {table}")
    
    return jsonify(table)

@app.route('/table', methods=['GET'])
def list_tables():
    """
    List all table resources. The result will be an array of the following objects:
    {
        id: string
        name: string
        size: number
        readOnly: boolean
    }
    """
    print("GET /table")
    return jsonify(tables)

@app.route('/table/<table_id>', methods=['GET'])
def get_table(table_id):
    """
    Return the table with the given id. The result will be an object of type:
    {
        id: string
        name: string
        size: number
        readOnly: boolean
    }
    """
    print(f"GET /table/{table_id}")
    table = next((t for t in tables if t["id"] == table_id), None)
    
    if not table:
        return error_response(404, "Not found")
    else:
        print(f"Returning table {table_id}")
        return jsonify(table)

@app.route('/table/<table_id>', methods=['PATCH'])
def update_table(table_id):
    """
    Patch (update) the given fields for the table with the given id. The input should
    be a JSON object in the form:
    {
        name?: string
        size?: number
        readOnly?: boolean
    }
    
    where only the fields given will be patched onto the table resource.
    """
    update = request.get_json()
    print(f"PATCH /table/{table_id} {update}")
    
    table = next((t for t in tables if t["id"] == table_id), None)
    
    if not table:
        return error_response(404, "Not found")
    
    # Validate and update fields
    for field in input_fields:
        if field["key"] not in update:
            continue
        
        if not validate_field_type(update[field["key"]], field["type"]):
            actual_type = type(update[field["key"]]).__name__
            return error_response(400, f"Field {field['key']} should be type {field['type']}, received type {actual_type}")
        
        table[field["key"]] = update[field["key"]]
    
    table["modifiedAt"] = datetime.now().isoformat()
    write_to_disk()
    print(f"Patched table {table_id}")
    
    return jsonify(table)

@app.route('/table/<table_id>', methods=['DELETE'])
def delete_table(table_id):
    """Delete a table resource."""
    global tables  # Move this to the top of the function
    
    print(f"DELETE /table/{table_id}")
    table = next((t for t in tables if t["id"] == table_id), None)
    
    if not table:
        return error_response(404, "Not found")
    else:
        print(f"Deleting table {table_id}")
        tables = [t for t in tables if t["id"] != table_id]
        write_to_disk()
        return jsonify(table)

if __name__ == '__main__':
    # Initialize data from disk
    read_from_disk()
    
    print(f"Mock service API listening at http://localhost:{port}")
    app.run(host='localhost', port=port, debug=True)

