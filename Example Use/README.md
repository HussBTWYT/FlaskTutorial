# Installation

To start off with installing the framework, make sure you have Python installed. Then, use the following command - please understand that this documentation is based on the Windows Operating System, so commands may be varied. 

~~~console
pip install flask
~~~

# Example Usage

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

When running this program, we see a similar line in your output, relating to this:

~~~
* Running on http://127.0.0.1:5000/
~~~

Now head over to http://127.0.0.1:5000/, and you should see your string on the website:

#### This is a string! Welcome to my website

# Note

Now that we have found out how we can actually return something, you can carry on **CLOSING DOWN YOUR SERVER**, then **MAKING SURE YOU SAVE YOUR PYTHON FILE** to run the server again, and access it there. 

We can fix the closing down your server issue every time, and only having to save your python file with the following edit to the last line:

Instead of the following:

~~~python
app.run()
~~~

We can say:

~~~python
app.run(debug=True)
~~~

This allows us to only need to save the file, then refresh our page on our website.

# Further Usage

For further usage, you can start off by editing the string to be anything you want, after testing around, we can carry on to develop our web application further.

We now need to establish a good defintion of: **routes**
A route, in any website, is a page displayed on websites. We have the default page, and additional pages.

What I mean is for instance, let's take www.youtube.com

www.youtube.com/ -> This slash is the default page, and isn't nessecary to write, this applies on every website, and you can even test it by removing the / from you running the server. We only do this just so we can actually render something, and not leave a blank string.

We also have: **www.youtube.com/trending**, which our secondary route is /trending

Using the code we made, can you guess on what our next lines will be, to have a similar /trending page, which renders a string e.g. "This is the trending page of our website!"

## Heres how we do it

~~~python
# Previous code is above
@app.route("/trending")
def trending_page():
      return "This is the trending page!"
~~~

Now, run your server, **AFTER ADDING THIS, AND NOT CHANGING THE WHOLE SCRIPT JUST DO THIS**, and go to 127.0.0.1:5000/trending to access our page, you should see the string inputted.

# HTML + Rendering the HTML template itself

- HTML = Hyper Text Markup Language

Go to any website, in the world, and inspect element it using the right click button on your mouse. You see all that random code, yes, as suprising as it sounds, it's not just there to change the amount of money you have in a game to flex to your friends, knowing your poor. Don't worry, we were all kids once.

HTML is used to display a variety of things in a website, like text, buttons, hyperlinks, input, forms, login forms, redirection, and positioning using CSS Styling or more - we will get to that soon - which is really useful.

**Let's remove our /trending route, and stick to our default page.**

Once we are back to our original script, start by going in your directory, and **creating a new folder called "templates"**

Then, create **a file in that folder templates, called "index.html"** so we can use HTML in our project.

If you don't know HTML, don't worry, just follow along, or copy and paste this code:

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our First Page</title>
</head>
<body>
    <h1>This is a new string</h1>
    <h2>This is a smaller string, woah!</h2>
    <h3>It's getting even smaller!</h3>
    <h4>Note: These are just headers, they aren't styling to make them smaller, they are programmed like this</h4>
    <p>This is a paragraph! Did you know the header element only goes down to 6? Anything other than that won't work!</p>
    <p>Also, know that every time you open <...> you must close it with the same thing, but a slash at the start</p>
</body>
</html>

~~~

Now, we aren't done here! Go back to your python script, and add this to the **first line of our script**

~~~python
from flask import Flask, render_template
~~~

After, go back to your route and **edit the default route function to this:**

~~~python
@app.route("/")
def welcome_page():
      return render_template("index.html")
~~~

Now, run the server, making sure you have a "templates" directory, and a index.html file inside it, and look, we say this:

# This is a new string
## This is a smaller string, woah!
### It's getting even smaller!
#### Note: These are just headers, they aren't styling to make them smaller, they are programmed like this
**This is a paragraph! Did you know only goes down to 6? Anything other than that won't work!**

**Also, know that every time you open <...> you must close it with the same thing, but a slash at the start**

With the title: Our First Page -> See this at the tab on top.

Let's do this with another route!

Let's add the following code to our script, just before the end, which creates a /secondpage, and returns a new HTML page.

### How to do this:

1. Go back to your templates folder/directory
2. Create a new HTML file called "secondpage.html" for instance, remember the name you chose by the way!
3. Go back to your python script, and add the following code:

~~~python
@app.route("/secondpage")
def second_page():
    return render_template("secondpage.html")
~~~

Then, for instance, make secondpage.html, look something like this:

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our First Page</title>
</head>
<body>
  <h1>Welcome to our second page</h1>
  <p>The following text I am about to give is called "filler words, it is gibberish, so don't get confused, it's just to show an example of what a paragraph will look like.</p>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
</body>
</html>
~~~

Again, when reading the website, you can see the gibberish is called filler words, to just fill up text for examples of paragraph.

Then you should be able to go on our first page (/) and see our previous code.

Then, go to /secondpage to see our next page.

# HTML Elements

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
