from flask import Blueprint, request, redirect, render_template
import os
import pandas as pd
import json
from utils.data_handler import save_questions
from config import UPLOAD_FOLDER

bp = Blueprint('upload', __name__)

@bp.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files['file']
        if file and file.filename.endswith('.xlsx'):
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            file.save(path)
            
            questions = []
            df = pd.read_excel(path)
            
            for idx, row in df.iterrows():
                entry = {
                    "id": int(row.get("id", idx+1)),
                    "question": row.get("question", "").strip(),
                    "options": json.loads(row["options"]) if pd.notna(row.get("options")) else {},
                    "answer": row.get("answer", "").strip(),
                    "explanation": row.get("explanation", "").strip()
                }
                questions.append(entry)
            
            save_questions(questions)
            return redirect("/bank")
    
    return render_template("upload.html")