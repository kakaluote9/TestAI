from flask import Flask
from routes import home, ask, bank, quiz, upload, download, history
import config

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