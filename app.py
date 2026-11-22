from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from extensions import db, login_manager
from flask import redirect, url_for



def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from routes.auth import auth
    from routes.dashboard import dashboard
    from routes.expenses import expenses

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(expenses)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

@app.route('/')
def home():
    return redirect(url_for('auth.login'))
if __name__ == '__main__':
    app.run(debug=True)
    