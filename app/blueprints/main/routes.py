# Main application blueprint
from flask import render_template
from app.blueprints.main import main


@main.route("/")
def home():
    return "Welcome to the Dummy Flask App!"
