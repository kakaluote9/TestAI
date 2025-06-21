from flask import Blueprint
import os
import pandas as pd
from config import HISTORY_FILE

bp = Blueprint('history', __name__)

@bp.route("/history")
def history():
    if not os.path.exists(HISTORY_FILE):
        return "暂无答题记录"
    
    df = pd.read_csv(HISTORY_FILE, names=["时间", "用户", "题目", "回答", "正确答案", "得分"])
    html = df.to_html(index=False)
    return f"<h2>答题历史记录</h2>{html}<a href='/'>返回主页</a>"