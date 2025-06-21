from flask import Flask
from routes import home, ask, bank, quiz, upload, download, history
import config
import os

app = Flask(__name__)
app.config.from_object(config)

# 注册蓝图
app.register_blueprint(home.bp)
app.register_blueprint(ask.bp)
app.register_blueprint(bank.bp)
app.register_blueprint(quiz.bp)
app.register_blueprint(upload.bp)
app.register_blueprint(download.bp)
app.register_blueprint(history.bp)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

"""

# 在 app 实例化后添加
if __name__ == "__main__":
    # 本地和 Netlify 都能使用的启动方式
    app.run(
        host='0.0.0.0', 
        port=int(os.environ.get("PORT", 5000)),
        debug=os.environ.get("FLASK_DEBUG") == "0"
    )

"""






