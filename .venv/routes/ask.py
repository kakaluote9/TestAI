from flask import Blueprint, request, render_template
from utils.ollama_helper import call_ollama

bp = Blueprint('ask', __name__)

@bp.route("/ask", methods=["GET", "POST"])
def ask():
    response = None
    if request.method == "POST":
        q = request.form.get("question")
        response = call_ollama(q)
    return render_template("ask.html", response=response)