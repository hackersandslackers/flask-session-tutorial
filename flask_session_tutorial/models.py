"""Database models."""

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from flask_session_tutorial import db


class User(UserMixin, db.Model):
    """User account database model."""

    __tablename__ = "flasksession-users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255), nullable=True)
    last_login = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User id={self.id}, name={self.name}, email={self.email}>"
