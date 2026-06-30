from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/") #default method is get and , Flask is neither GET nor POST by itself. Flask receives whatever request the browser sends.
def home():
    return render_template("fuki.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"] #acessing only username from the whole requestpackage
    password = request.form["password"]

    return f"Welcome {username}"

if __name__ == "__main__":
    app.run(debug=True)




"""
request (Backpack)

🎒
├── 📁 form      → Data from HTML forms
├── 📁 args      → Data from the URL
├── 📁 files     → Uploaded files
├── 📁 cookies   → Cookies
├── 📁 headers   → HTTP headers
└── 📁 json      → JSON data

"""





