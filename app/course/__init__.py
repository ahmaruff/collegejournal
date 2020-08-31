"""
(blueprint) This module provide course feature

this module use url_prefix = /course

views/route:
    /               : index/course main page (also include add-course feature)
    /remove/<id>    : remove existing course

templates directory:
    templates/course/
"""

from flask import Blueprint

course = Blueprint('course', __name__)

from . import views