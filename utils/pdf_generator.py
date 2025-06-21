from fpdf import FPDF
import os
from config import UPLOAD_FOLDER

def generate_pdf(questions):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for q in questions:
        pdf.multi_cell(0, 10, f"Q{q['id']}: {q['question']}\n答：{q['answer']}\n解释：{q['explanation']}\n")
    out_path = os.path.join(UPLOAD_FOLDER, "题库导出.pdf")
    pdf.output(out_path)
    return out_path