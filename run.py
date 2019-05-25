# 5. Import os from the standard Python library
import os

# 1. Import the Flask class from the flask library - Capital 'F' indicates class name
from flask import Flask

# 2. Create an instance of Flask class - convention in Python is to call the variable app
# First argument of Flask class is name of the application's module or package
# If using a single module, we use (__name__) which is built in Python variable
# Flask needs this so it knows where to look for templates and static files
app = Flask(__name__)

# 3. Using the app.route() decorator - starts with an @ sign, a.k.a py notation
# Decorator is a way of wrapping functions - when we try to browse to the root directory,
# as indicated by "/", flask triggers the functions underneath it
@app.route("/")

# 4. Create function
def index():
    return "Hello, World!"

# 6. Reference the built in variable and say if __name__ is equal to "__main__"
# we will run our app with the following arguments
# __main__ is the name of the default module in Python, the first one that we run
if __name__ == "__main__":
    # Internal environment variable that Cloud9 has set, and we're using os to get it for us
    app.run(host=os.environ.get("IP"),
            # Same with port, but it needs to be an integer
            port=int(os.environ.get("PORT")),
            # This allows us to debug our code easier
            # ***This should only be used in the test environment, not the live environment***
            debug=True)