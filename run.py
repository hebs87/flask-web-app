# 5. Import os from the standard Python library
import os

# 1. Import the Flask class from the flask library - Capital 'F' indicates class name
# 7. Import render_template function to render HTML
from flask import Flask, render_template

# 2. Create an instance of Flask class - convention in Python is to call the variable app
# First argument of Flask class is name of the application's module or package
# If using a single module, we use (__name__) which is built in Python variable
# Flask needs this so it knows where to look for templates and static files
app = Flask(__name__)

# 3. Using the app.route() decorator - starts with an @ sign, a.k.a py notation
# Decorator is a way of wrapping functions - when we try to browse to the homepage,
# as indicated by "/", flask triggers the functions underneath it
@app.route("/")

# 4. Create index() function where we want to run our data from
# 8. Reference render_template and HTML page (created in templates directory)
def index():
    # We can type HTML directly into our return. eg return "<h1>Hello, World!</h1>"
    # which is time consuming, so we use render_template instead
    return render_template("index.html")

# 9. Create another route to about.html page
@app.route("/about")

# 10. Create about() function that is called each time we navigate to about.html
# ***The href links in the HTML pages need to have the same function name in them***
def about():
    return render_template("about.html")

# 11. Create another route to the contact.html page, and a contact() function
@app.route("/contact")
def contact():
    return render_template("contact.html")

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