from flaskext.script import Manager
from frontend import create_app
from frontend.extensions import db

app = create_app()

manager = Manager(app)

@manager.command
def run():
  app.run()

@manager.command
def reset():
  db.drop_all()
  db.create_all()

if __name__ == "__main__":
  manager.run()
