#main module

from flask import Flask
from self.suth_folder.auth import auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.run(debug = True)