from flask import Blueprint, request, redirect, render_template, json
from utils.data_handler import load_questions, add_question, update_question, delete_question

bp = Blueprint('bank', __name__)

@bp.route("/bank")
def bank():
    questions = load_questions()
    return render_template("bank.html", questions=questions)

@bp.route("/add", methods=["POST"])
def add():
    questions = load_questions()
    try:
        questions = add_question(questions, request.form)
        return redirect("/bank")
    except json.JSONDecodeError:
        return "<h3>选项(JSON)格式错误，请检查后再提交。</h3><a href='/bank'>返回</a>"

@bp.route("/update", methods=["POST"])
def update():
    questions = load_questions()
    try:
        questions = update_question(questions, request.form)
        return redirect("/bank")
    except json.JSONDecodeError:
        return "<h3>选项(JSON)格式错误，请检查后再提交。</h3><a href='/bank'>返回</a>"

@bp.route("/delete", methods=["POST"])
def delete():
    questions = load_questions()
    try:
        qid = int(request.form["id"])
        questions = delete_question(questions, qid)
        return redirect("/bank")
    except Exception as e:
        return f"<h3>删除失败：{e}</h3><a href='/bank'>返回题库</a>"

@bp.route("/edit", methods=["POST"])
def edit():
    questions = load_questions()
    try:
        qid = int(request.form["id"])
        q = next((q for q in questions if q.get("id") == qid), None)
        if q:
            return render_template("edit.html", q={
                "id": qid,
                "question": q.get("question", ""),
                "options": json.dumps(q.get("options", {}), ensure_ascii=False),
                "answer": q.get("answer", ""),
                "explanation": q.get("explanation", "")
            })
        else:
            return "<h3>未找到对应题目</h3><a href='/bank'>返回题库</a>"
    except Exception as e:
        return f"<h3>编辑加载失败：{e}</h3><a href='/bank'>返回题库</a>"