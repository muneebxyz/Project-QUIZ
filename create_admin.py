from quiz_app.models import User
from main import app
from quiz_app.extentions import db


name = "admin"
password = "admin"


with app.app_context():
    u = User.query.filter_by(
        name=name
    ).first()
    if u is None:
        user = User(
            name=name,
            password=password,
            is_admin=True
        )
        db.session.add(user)
        db.session.commit()
        print(
            f"Administer created successfully... {user}"
        )
    else:
        print(
            f"A user already exists with the name {name}",
        )
