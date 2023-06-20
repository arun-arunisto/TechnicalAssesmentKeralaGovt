from user_creation.user_blueprint import user_bp
from user_creation.models import db
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "arunisto"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:arunisto@localhost/keralaproject'
db.init_app(app)

with app.app_context():
    db.create_all()
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)
