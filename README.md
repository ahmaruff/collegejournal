# Flask-Jurnalkuliah
a simple college-journal entries app, made with flask.


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
1. Python 3.8 or later
2. Text Editor (VS-Code/Pycharm/Sublime/etc)
3. Git

### Instalation
1. Install all prerequisites app above
2. Clone this project to your local machine. [how to](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
3. create new venv (virtual environment) inside this project directory on your local machine. [how to](https://docs.python.org/3/library/venv.html)
4. Download & install required library in requirements.txt  
  a. Open terminal  
  b. Activate your venv,[how to](https://docs.python.org/3/library/venv.html)  
  c. go to your working directory (this project directory) and run this command    
    
    ```
    for windows :  
    $ python -m pip install -r requirements.txt
    
    for Linux :
    $ pip install -r requirements.txt
    ```

## Initial Configuration

### Database Setup
1. open `config.py`  
change Database URI to Correct `DATABASE_URI` that you want to use. Especially on `DevelopmentConfig` (since you are using this project for development purpose.)
take a look to [this page](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/) for more information.

  ```
  import os

  basedir = os.path.abspath(os.path.dirname(__file__))
  ####
  
  class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
          # pick one database URI that you want to use. (sometimes you need some other external library,  this is depends on your setup)
          'mysql://username:password@localhost/yourdatabase'
          'postgresql://usernamepasswordr@localhost/mydatabase'
          'oracle://username:pasword@127.0.0.1:1521/sidname'
          'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
   ```
   
   
### Create Database Table  
  a. open terminal, move to working directory, and activate your venv.  
  b. setup environment variable so flask can run,

  ```
  on Linux:
  $ export FLASK_APP=journal.py
  $ export FLASK_CONFIG='development'
  
  on Windows CMD:
  $ set FLASK_APP='journal.py'
  $ set FLASK_CONFIG='development'
  
  on Windows Powershell:
  $ $env:FLASK_APP='journal.py'
  $ $env:FLASK_CONFIG='development'

  ```  
  
  c. run `flask shell` on your terminal, (note the terminal icon change from `$` to `>>>`)  
  d. run this command:
  
  ```
    from journal import db (click enter)
    
    db.create_all() (click enter)
    
    quit() (click enter to quit shell)
  ```

## Start Your Flask App
  1. open terminal, move to working directory, and activate your venv.
  2. setup environment variable so flask can run,
  
  ```
  on Linux:
  $ export FLASK_APP=journal.py
  $ export FLASK_CONFIG='development'
  
  on Windows CMD:
  $ set FLASK_APP='journal.py'
  $ set FLASK_CONFIG='development'
  
  on Windows Powershell:
  $ $env:FLASK_APP='journal.py'
  $ $env:FLASK_CONFIG='development'
  ```
  
  3. run this command on your terminal
    `flask run`
  
  4. if there's no problem, your terminal will show your web information and Debugging information. you web will run on localhost or 127.0.0.1 and use port number 5000
  
  5. try open browser and access `http://localhost:5000`
          
## Production Deployment  
> Currently we did not spend lot of time on security, so we did not recomend deploying this app into production.  
> There's no `registration token` for new-user registration yet, so please think wisely if you want to deploy this app into production. or we'll be very gratefull if you could contribute adding this feature to this app.    

These are reference link about how to deploy this app into [pythonanywhere](https://pythonanywhere.com)  
- [how to deploy existing django app to pythonanywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)  
- [setting up flask application on pythonanywhere](https://help.pythonanywhere.com/pages/Flask/)  

If you need to use `Environment Variables` to setup your app, please refer to [this page](https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/)  

### Database Setup on Pythonanywhere
1. Create new database from database menu on Pythonanywhere dashboard.
2. declare your database to `config.py`, especially on `ProductionConfig`
  ```
  `mysql+mysqldb://username:password@database-host-address/yourdatabase`
  
  in pythonanywhere its often looks like this:  
  `mysql+mysqldb://yourusername:databasepassword@yourusername.mysql.pythonanywhere-services.com/yourusername$database'
  ```
3. **Create Database Tables**  
  a. open bash console from pythonanywhere dashboard.  
  b. activate you venv  
     `workon your-venv`  
  c. move to project directory  
    `cd myproject`  
    d. run `flask shell` on your terminal, (note the terminal icon change from $ to >>>)  
    e. run this command    
    ```
    from journal import db
    db.create_all()
    ```  
    f. your database ready to use
  
> There's no big different on configuring for Production and Development. you just need to take more attention on Database Connection and ofcourse, **Security**  

## Build With
- [Python](https://www.python.org) -Programing Language that used.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) -Web Framework that used

## Author
- [Ahmad Ma'ruf](https://github.com/ahmaruff)  
           
           
           
