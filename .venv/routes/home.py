from flask import Blueprint, render_template
from utils.data_handler import load_questions

bp = Blueprint('home', __name__)

@bp.route("/")
def home():
    return render_template("home.html")