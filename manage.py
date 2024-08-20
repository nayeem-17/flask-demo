from flask import Flask
from app import create_app
from flask_migrate import Migrate
from app.utils.database import db

app = create_app()
migrate = Migrate(app, db)


@app.cli.command("seed")
def seed():
    """Seed the database with initial data."""
    from app.models.user import User  # Import your models

    user = User(username="admin")
    db.session.add(user)
    db.session.commit()
    print("Database seeded with initial data.")


if __name__ == "__main__":
    app.run()
