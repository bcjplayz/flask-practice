from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def menu():
    return """
    <h1>Welcome to my page</h1>
    <ul>
    <li><a href="/home">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/hobbies">Hobbies</a></li>
    <li><a href="/contact">Contact</a></li>
    </ul>
    """
 
@app.route("/about")
def about():
    return "<h3>My name is Bailey Woodward and i am studying a digital course at Bolton College</h3>"
 
@app.route("/hobbies")
def hobbies():
    return """<h2>My hobbies include:</h2>
    <ul>
    <li>Drawing</li>
    <li>Gaming</li>
    <li>Anime</li>
    """
 
@app.route("/contact")
def contact():
    return "My email address is bcjplayz@gmail.com"
 
@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}, welcome to my website!"

@app.route("/age/<int:years>")
def age():
    return f"<h2>In 10 years you will be {age+10}</h2>"

@app.route("/repeat/<word>/<int:amount>")
def loop(word, amount):
    word += ""
    return f"<h1>{word * amount}</h1>"

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return f"""{a+b=}"""

@app.route("/subtract/<int:a>/<int:b>")
def subtract(a,b):
    return f"""{a-b=}"""

@app.route("/divide/<int:a>/<int:b>")
def divide(a,b):
    if a == 0 or b == 0:
        return ("<p>Cannot divide by 0</p>")
    else:
        return f"""{a/b=}"""

@app.route("/multiply/<int:a>/<int:b>")
def multiply(a,b):
    if a == 0 or b == 0:
        return ("<p>Cannot multiply nothing</p>")
    else:
        return f"""{a*b=}"""

if __name__ == "__main__":
    app.run(debug=True)