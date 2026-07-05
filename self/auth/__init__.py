#used to aviod hardcodding in every import
from flask import Blueprint

auth_bp = Blueprint(
    "auth",
    __name__
    , url_prefix="/auth"
)

from . import routes