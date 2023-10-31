# Installation

To start off with installing the framework, make sure you have Python installed. Then, use the following command - please understand that this documentation is based on the Windows Operating System, so commands may be varied. 

~~~console
pip install flask
~~~

# Setup Files

We can create a starter file, by creating a new directory to your choice's name, e.g. "mywebsite" for instance, and create the following:

- app.py

We will look into adding a /templates, and then a /templates/file.html shortly.

~~~python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome_page():
  return "This is a string! Welcome to my website."

app.run()
~~~


