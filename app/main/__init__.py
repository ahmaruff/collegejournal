"""
(blueprint) This module provide main feature

views/route:
    /                   : index (front page)
    /about              : about this web
    /profile/username   : user profile
    /edit-profile       : edit user profile
    /markdown-guide     : guide how to writing markdown

error handling:
    404, 500, 403

templates directory:
    templates/main/
"""

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors