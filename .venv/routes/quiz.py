from flask import Blueprint, request, render_template
from utils.data_handler import load_questions, is_similar, record_history
from datetime import datetime

bp = Blueprint('quiz', __name__)

@bp.route("/quiz", methods=["GET", "POST"])
def quiz():
    questions = load_questions()
    
    if request.method == "GET":
        username = request.args.get("user", "anonymous")
        return render_template("quiz.html", questions=questions, user=username)
    else:
        score = 0
        results = []
        user = request.form.get("user", request.remote_addr or "anonymous")
        
        for q in questions:
            user_answer = request.form.get(f"q{q['id']}", "未作答")
            correct = q['answer']
            
            if q['options']:
                correct_flag = user_answer == correct
            else:
                correct_flag = is_similar(user_answer, correct)
                
            if correct_flag:
                score += 1
                
            results.append({
                "question": q['question'],
                "your_answer": user_answer,
                "correct_answer": correct,
                "explanation": q['explanation']
            })
        
        record_history(user, results, score)
        return render_template("result.html", 
                              score=score, 
                              total=len(questions), 
                              results=results)