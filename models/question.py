QUESTION_FILE = "questions.json"
HISTORY_FILE = "history.csv"
question_bank = []
if os.path.exists(QUESTION_FILE):
    with open(QUESTION_FILE, encoding="utf-8") as f:
        question_bank = json.load(f)