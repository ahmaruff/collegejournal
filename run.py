import os
from app import create_app, db
from app.models import Student, Course, Journal
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# create_app function is used to create app using configuration based on config.py,
# or default : DevelopmentConfig().
# this can be set using virtual environment "FLASK_CONFIG",
# the value must be development, production, or testing

migrate = Migrate(app, db)
# create migration on Database changes, similar to Git, but for database.
# using flask-migrate library

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,Student=Student, Course=Course, Journal=Journal)

# create flask-shell context, you can call it directly from run.py instead call from app.models,
# 
# ex: $ flask shell
#   >>> from run import db, Student, Course, Journal
#       
# this is same as
#     $ flask shell
#   >>> from app import db
#   >>> from app.models import Student, Course, Journal