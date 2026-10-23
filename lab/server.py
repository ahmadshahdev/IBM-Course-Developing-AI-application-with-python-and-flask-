# Import the Flask class from the flask module
from flask import Flask, make_response

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)


#----------- part 0 ---------------

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"


# --------Part 1: Return a custom HTTP status code using a tuple -------------

# @app.route("/no_content")
# def no_content():
#     """return 'No content found' with a status of 204

#     Returns:
#         string: No content found
#         status code: 204
#     """
#     return ({"message": "No content found"}, 204)


# -------------Part 2: Return a custom HTTP response using make_response()-----------

@app.route("/exp")
def index_explicit():
    """return 'Hello World' using make_response with a status of 200"""
    res = make_response({"message": "Hello World"})
    res.status_code = 200
    return res

if __name__ == "__main__":
    app.run(debug=True)