from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def show_datetime():
    now = datetime.now()
    date_time = now.strftime("%d.%m.%Y %H:%M:%S")
    return f"<h1>Текущие дата и время:</h1><p>{date_time}</p>"

if __name__ == "__main__":
    app.run(debug=True)
