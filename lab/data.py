from flask import Flask, request, make_response
from uuid import UUID



app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

# -----------------DEMO---------------


# @app.route("/data")
# def get_data():
#     try:
#         # Check if 'data' exists and has a length greater than 0
#         if data and len(data) > 0:
#             # Return a JSON response with a message indicating the length of the data
#             return {"message": f"Data of length {len(data)} found"}
#         else:
#             # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
#             return {"message": "Data is empty"}, 500
#     except NameError:
#         # Handle the case where 'data' is not defined
#         # Return a JSON response with a 404 Not Found status code
#         return {"message": "Data not found"}, 404



# --------------------Process input arguments--------------------- 
# --------------------MY TASK ---------------------


# @app.route("/name_search")
# def name_search():
#     """Find a person in the database based on the provided query parameter.

#     Returns:
#         json: Person if found, with status of 200
#         404: If not found
#         400: If the argument 'q' is missing
#         422: If the argument 'q' is present but invalid (e.g., empty or numeric)
#     """
#     # Get the 'q' query parameter from the request URL
#     query = request.args.get("q")

#     # Check if the query parameter 'q' is missing
#     if query is None:
#         return {"message": "Query parameter 'q' is missing"}, 400
    
#     # Check if the query parameter is present but invalid (empty or numeric)
#     if query.strip() == "" or query.isdigit():
#         return {"message": "Invalid input parameter"}, 422
    
#     # Iterate through the 'data' list to search for a matching person
#     for person in data:
#         # Check if the query string is present in the person's first name (case-insensitive)
#         if query.lower() in person["first_name"].lower():
#             # Return the matching person as a JSON response with a 200 OK status code
#             return person, 200
#     return {"message": "Person not found"}, 404

# -------------------------------------------------------------------------------------------------


#-------------------Add dynamic URLs---------------------------------------

#-------------------- Task 1: Create GET /count endpoint------------------------------------

@app.route("/count")
def count():
    """Return the total number of items in the data list."""
    return {"count": len(data)}, 200



# ----------------------------Task 2: Create GET /person/id endpoint-----------------------


@app.route("/person/<uuid:id>", methods=["GET"])
def find_by_uuid(id):
    """Find a person by UUID and return their details.
    
    Flask's <uuid:id> converter ensures 'id' is automatically validated 
    and passed as a Python UUID object.
    """
    person_id_str = str(id)
    
    # Search for matching UUID string in data
    for person in data:
        if person.get("id") == person_id_str:
            return person, 200
            
    # Return HTTP 404 if not found
    return {"message": "person not found"}, 404


#----------------------Task 3: Create DELETE /person/id endpoint------------------

@app.route("/person/<uuid:id>", methods=["DELETE"])
def delete_by_uuid(id):
    """Delete a person resource from data by UUID."""
    person_id_str = str(id)
    
    # Find the person matching the UUID and remove them
    for person in data:
        if person.get("id") == person_id_str:
            data.remove(person)
            return {"message": f"Person with ID {person_id_str} deleted"}, 200
            
    # Return HTTP 404 if the UUID was not found in data
    return {"message": "person not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)