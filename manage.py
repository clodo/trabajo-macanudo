import os
from flaskext.script import Manager
from frontend import create_app
from frontend.extensions import db

app = create_app()

manager = Manager(app)

@manager.command
def run():
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)

@manager.command
def reset():
  db.drop_all()
  db.create_all()

if __name__ == "__main__":
  manager.run()
