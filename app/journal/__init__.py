"""
(blueprint) This module provide journal feature

this module use url_prefix = /journal

views/route:
    /               : index (journal main page)
    /<id>           : single journal page (permalink)
    /add            : add new journal
    /edit/<id>      : edit existing journal
    /remove/<id>    : remove existing journal

templates directory:
    templates/journal/
    
"""

from flask import Blueprint

journal = Blueprint('journal', __name__)
from . import views
