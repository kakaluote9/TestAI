import json
import os
from config import JSON_FILE, HISTORY_FILE
from difflib import SequenceMatcher

# 初始化题库
def load_questions():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_questions(questions):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

def add_question(questions, form_data):
    new_id = max([q['id'] for q in questions], default=0) + 1
    questions.append({
        "id": new_id,
        "question": form_data["question"],
        "options": json.loads(form_data["options"] or "{}"),
        "answer": form_data["answer"],
        "explanation": form_data["explanation"]
    })
    save_questions(questions)
    return questions

def update_question(questions, form_data):
    qid = int(form_data["id"])
    for q in questions:
        if q["id"] == qid:
            q["question"] = form_data["question"]
            q["options"] = json.loads(form_data["options"] or "{}")
            q["answer"] = form_data["answer"]
            q["explanation"] = form_data["explanation"]
    save_questions(questions)
    return questions

def delete_question(questions, qid):
    questions = [q for q in questions if q.get("id") != qid]
    save_questions(questions)
    return questions

def is_similar(ans1, ans2, threshold=0.7):
    return SequenceMatcher(None, ans1.lower().strip(), ans2.lower().strip()).ratio() >= threshold

def record_history(user, results, score):
    from datetime import datetime
    timestamp = datetime.now().isoformat()
    with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
        for r in results:
            line = f"{timestamp},{user},{r['question'].replace(',', ' ')},{r['your_answer'].replace(',', ' ')},{r['correct_answer']},{score}\n"
            f.write(line)