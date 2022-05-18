from app import create_app, db
from app.models import User, Blog

# Creating app instance
app = create_app()


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Blog=Blog)


if __name__ == '__main__':
    app.run()
