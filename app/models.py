from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from app import db, login


class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String(120), unique=True)
    first_name: str = db.Column(db.String(15))
    last_name: str = db.Column(db.String(15))
    password_hash: str = db.Column(db.String(128))
    created_at: datetime = db.Column(db.DateTime(), default=datetime.utcnow())

    def __repr__(self):
        return f"<Users {self.id}>"

    def set_password(self, password: str) -> bool:
        """
        Sets the password hash for the user.

        :param password: password to hash
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """
        Checks if the given password matches the user's password hash.

        :param password: password to check
        :return: True if the password matches, False otherwise
        """
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    """
    Loads a user from the database (used by Flask-Login).

    :param id: user ID
    :return: user object
    """
    return Users.query.get(int(id))
