'''__main__ is a special Python name that tells you:

"Is this file being run directly, or is it being imported by another file?"'''



print(__name__)

#we use to run using hardcoding


from flask import Flask
app = Flask (__name__)  # create an object app via the flsk class, act as starting point to find the other folder like templates... layman it creeate existence of the WEBSITE 
@app.route('/')
def hellow_world():
    return "hellow world"

if __name__ == "__main__":
    app.run()