#import the flask class form the flask application

from flask import Flask, render_template 



app = Flask(__name__) #store all MF data here


#add html file
@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)

#add img in that html file