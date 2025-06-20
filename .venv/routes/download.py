from flask import Blueprint, send_file
import os
import pandas as pd
from utils.data_handler import load_questions
from utils.pdf_generator import generate_pdf
from config import UPLOAD_FOLDER, HISTORY_FILE

bp = Blueprint('download', __name__)

@bp.route("/download/csv")
def download_csv():
    questions = load_questions()
    df = pd.DataFrame(questions)
    csv_path = os.path.join(UPLOAD_FOLDER, "题库导出.csv")
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')
    return send_file(csv_path, as_attachment=True)

@bp.route("/download/pdf")
def download_pdf():
    questions = load_questions()
    pdf_path = generate_pdf(questions)
    return send_file(pdf_path, as_attachment=True)