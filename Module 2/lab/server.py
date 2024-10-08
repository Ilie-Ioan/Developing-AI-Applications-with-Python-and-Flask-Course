
from flask import Flask,request


app = Flask(__name__)

@app.route("/data")

def get_data():
    try:
        if data and len(data) > 0:
            return {"messsage": f"Data of length {len(data)} found"}
        else:
            return {"message": f"Data is empty"},500
    except NameError:
        return{"message":"Data not found"},400
@app.route('/find_person')

def find_person():
    """Find a person in the database.
    Returns:
        json: Person if found, with status of 200
        404: If not found
        422: If argument 'q' is missing
    """
    query = request.args.get('q')
    if not query:
        return {"message": "Query parameter 'q' is missing"}, 422
    for person in data:
        if query.lower() in person["first_name"].lower():
            return person
    return {"message": "Person not found"}, 404
@app.route("/count")

def count():
    try:
        return {"data count": len(data)}, 200
    except NameError:
        return {"message": "data not defined"}, 500
@app.route("/person/<uuid:id>")

def find_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            return person
    return {"message": "person not found"}, 404
@app.route("/person/<uuid:id>", methods=['DELETE'])

def delete_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            data.remove(person)
            return {"message": f"Person with ID {id} deleted"}, 200
    return {"message": "person not found"}, 404

@app.route("/person", methods=['POST'])

def add_by_uuid():
    new_person = request.json
    if not new_person:
        return {"message": "Invalid input parameter"}, 422
    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500
    return {"message": f"{new_person['id']}"}, 200

@app.errorhandler(404)
def api_not_found(error):
    return {"message": "API not found"}, 404