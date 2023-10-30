from flask import Flask

app = Flask(__name__)

@app.route("/") # / = The default HOMEPAGE of every single website, in the world (type: decorator)
def index():
  return "Hello, World!" # This is converted right into a HTML template, so using specific elements e.g. <h1> would make it a header.

app.run() # Remove if commercial, search for your hostings website documentation on how you can remove this, while keeping the whole project succesfully running.
  
