from app import createapp, db
from app.models import User, Blog
from flask_migrate import Migrate

# Creating app instance
app = createapp('development')
app = createapp('production')

migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Blog=Blog)


if __name__ == '__main__':
    app.run()
