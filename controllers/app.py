import os
from flask import Flask
from jinja2 import Environment, FileSystemLoader
from random import randint

# Start the Flask application

app = Flask(__name__, static_path='/static')

# Define the template directory
tpldir = os.path.dirname(os.path.abspath(__file__))+'/templates/'

# Setup the template enviroment
env = Environment(loader=FileSystemLoader(tpldir), trim_blocks=True)

# Define a route for the webserver
@app.route('/')
def index():
  
  # define a random skill level
  bind = randint(0,100)
  #bind = 0
  renderWith0 = 'true'

  dateTimeList =[1,2,3,4,5,6]
      
  # generate template and assign variables
  output = env.get_template('index.html').render(
    bind=bind,renderWith0=renderWith0,dateTimeList=dateTimeList
  )
  
  # return the output
  return output


if __name__ == '__main__':
    app.debug=True
    app.run()