"""
(blueprint) This module provide authentication feature

this module use url_prefix = /auth

views/route:
    /login              : login page
    /logout             : user logout
    /register           : user registration
    /unconfirmed        : unconfirmed-account landing page
    /confirm            : confirmation account
    /confirm/<token>    : generate confirmation token
    /resetpassword_req  : request password reset
    /reset_password/<token> : reset password form 

templates directory:
    templates/auth/
"""


from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views