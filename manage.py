import os
from flask import current_app
from flaskext.script import Manager
from frontend import create_app, models
from frontend.emailForwarder.emailReader import EmailForwardService, EmailKeyReader, PostulacionGetEmailByEmailKeyQuery, EmailRepository, ForwardEmailBuilder
from frontend.extensions import db


manager = Manager(create_app)

manager.add_option('-c', '--config', dest='config', required=False)

@manager.command
def run():
  port = int(os.environ.get('PORT', 5000))
  current_app.run(host='0.0.0.0', port=port)

@manager.command
def reset():
  db.drop_all()
  db.create_all()

from frontend.models import Macanudo

@manager.command
def runEmailForward():
    forwardService = EmailForwardService(EmailRepository(),PostulacionGetEmailByEmailKeyQuery(), EmailKeyReader, ForwardEmailBuilder)
    forwardService.forwardAll()



if __name__ == "__main__":
     manager.run()
