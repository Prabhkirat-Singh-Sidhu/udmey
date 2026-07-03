from . import auth_bp

@auth_bp.route("/login")
def login():
    return "login page"

@auth_bp.routes("/register")
def register():
    return "Register Page"
